<template>
  <div class="card card-custom">
    <!--begin::Header-->
    <div class="card-header py-3">
      <div class="card-title align-items-start flex-column">
        <h3 class="card-label font-weight-bolder text-dark">Outlook Integration</h3>
        <span class="text-muted font-weight-bold font-size-sm mt-1"
          >Connect to Outlook</span
        >
      </div>
      
      <div class="card-toolbar">
        <button
          class="btn btn-success mr-2"
          ref="kt_save_changes"
          @click="Integrate"
        >
          Save
        </button>
        <button
          class="btn btn-primary mr-2"
          ref="kt_save_changes"
          @click="changeView"
        >
          Cancel
        </button>
      </div>
    </div>
    <!--end::Header-->
    <!--begin::Form-->
      <div class="card-body">
            <v-form
                ref="microsoft_form"
                v-model="microsoft_valid"
                lazy-validation
                >
                <v-row class="mb-3">
                    <v-col>
                        <v-text-field
                            v-model="microsoft_email"
                            :rules="[rules.required, rules.email]"
                            class="form-control form-control-lg form-control-solid"
                            label="E-mail*"
                        ></v-text-field>
                    </v-col>
                    <v-col>
                        <v-text-field
                            v-model="microsoft_username"
                            :rules="[rules.required]"
                            label="User Name*"
                            class="form-control form-control-lg form-control-solid"
                            :readonly="microsoft_username_disable"
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-row class="mx-0 mb-2">
                    <v-text-field
                        v-model="microsoft_emails_per_day"
                        label="No of emails your email provider allows you to send per day"
                        :rules="[rules.required, rules.emails]"
                        class="form-control form-control-lg form-control-solid"
                        type="number"
                    ></v-text-field>
                </v-row>
                <v-row>
                    <span class="switch switch-icon ml-6 mr-3">
                        <label>
                        <input type="checkbox" v-model="microsoft_switch" @change="microsoft_switch_change" />
                        <span></span>
                        </label>
                    </span>
                    <span class="my-7">Click here if your username is the same as your email</span>
                </v-row>
            
                <v-row>
                    <v-col class="mx-4">
                        <v-row class="mx-6 my-4">
                            <span class="mt-3 font-weight-medium text--secondary">Recieving emails</span>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                v-model="microsoft_IMAP_HOST"
                                label="IMAP Host"
                                class="form-control form-control-lg form-control-solid"
                                readonly
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                v-model="microsoft_IMAP_Port"
                                label="IMAP Port"
                                class="form-control form-control-lg form-control-solid"
                                readonly
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                :append-icon="microsoft_IMAP_show ? 'mdi-eye' : 'mdi-eye-off'"
                                :rules="[rules.required]"
                                :type="microsoft_IMAP_show ? 'text' : 'password'"
                                label="Password"
                                class="form-control form-control-lg form-control-solid input-group--focused"
                                v-model="microsoft_IMAP_password"
                                @click:append="microsoft_IMAP_show = !microsoft_IMAP_show"
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-select
                                v-model="microsoft_IMAP_options"
                                :items="microsoft_OPTIONS"
                                prepend-inner-icon="mdi-earth"
                                class="form-control form-control-lg form-control-solid"
                                readonly
                            ></v-select>
                        </v-row>
                    </v-col>
                    <v-col class="mx-4">
                        <v-row class="mx-6 my-4">
                            <span class="mt-3 font-weight-medium text--secondary">Sending emails</span>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                v-model="microsoft_SMTP_HOST"
                                label="SMTP Host"
                                class="form-control form-control-lg form-control-solid"
                                readonly
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                v-model="microsoft_SMTP_Port"
                                label="SMTP Port"
                                class="form-control form-control-lg form-control-solid"
                                readonly
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                :append-icon="microsoft_SMTP_show ? 'mdi-eye' : 'mdi-eye-off'"
                                :rules="[rules.required]"
                                :type="microsoft_SMTP_show ? 'text' : 'password'"
                                label="Password"
                                v-model="microsoft_SMTP_password"
                                class="form-control form-control-lg form-control-solid input-group--focused"
                                @click:append="microsoft_SMTP_show = !microsoft_SMTP_show"
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-select
                                v-model="microsoft_SMTP_options"
                                :items="microsoft_OPTIONS"
                                prepend-inner-icon="mdi-earth"
                                class="form-control form-control-lg form-control-solid"
                                readonly
                            ></v-select>
                        </v-row>
                    </v-col>
                </v-row>
            </v-form>
        </div>
    <!--end::Form-->
  </div>
</template>

<script>
import store from "@/core/services/store/store.js";
import axios from "axios";
import Vue from 'vue';
import VueCookies from 'vue-cookies';
import Swal from "sweetalert2";
Vue.use(VueCookies)

export default {
  name: "Outlook",
  data: () => {
    return {
        rules: {
            required: value => !!value || 'Required.',
            email: value => {
                const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                return pattern.test(value) || 'Invalid e-mail.'
            },
            less_than: value => value <= 65535 || 'Invalid port number',
            greater_than: value => value >= 0 || 'Invalid port number',
            emails: value => value > 0 || 'number of emails cannot be less than 1',
        },

        microsoft_show: false,
        microsoft_IMAP_show: false,
        microsoft_IMAP_password: '',
        microsoft_IMAP_HOST: 'outlook.office365.com',
        microsoft_IMAP_Port: 993,
        microsoft_IMAP_options: 'Enable SSL',
        microsoft_SMTP_show: false,
        microsoft_SMTP_password: '',
        microsoft_SMTP_HOST: 'smtp.office365.com',
        microsoft_SMTP_Port: 587,
        microsoft_SMTP_options: 'STARTTLS',
        microsoft_OPTIONS: ['Enable SSL','STARTTLS'],
        microsoft_emails_per_day: 300,

        microsoft_email: '',
        microsoft_sender_name: '',
        microsoft_username_disable: false,
        microsoft_switch: false,
        microsoft_valid: true
    };
  },
  beforeMount(){
      
  },
  methods: {
    changeView(){
          store.state.integration.view = 0;
      },
    Integrate(){
        if(this.$refs.microsoft_form.validate()){
            var data = {
                'email': this.microsoft_email,
                'username': this.microsoft_sender_name,
                'IMAP_password': this.microsoft_IMAP_password,
                'IMAP_host': this.microsoft_IMAP_HOST,
                'IMAP_type': this.microsoft_IMAP_options,
                'IMAP_port': this.microsoft_IMAP_Port,
                'smtp_host': this.microsoft_SMTP_HOST,
                'smtp_port': this.microsoft_SMTP_Port,
                'smtp_password': this.microsoft_SMTP_password,
                'smtp_type': this.microsoft_SMTP_options,
                'emails_per_day': this.microsoft_emails_per_day
            }
            axios.defaults.baseURL = "http://127.0.0.1:8000/";
            axios.defaults.headers.post["Content-Type"] = "application/json";
            axios.defaults.headers.common["Authorization"] =
                "Token " + Vue.$cookies.get("key");
            axios
                .post("api/user/outlook/connect/", data)
                .then(function () {
                    store.state.integration.view = 0;
                })
                .catch(function (error) {
                if (error.response) {
                    Swal.fire({
                    title: "Error",
                    text: "Failed to update Password!",
                    icon: "error",
                    confirmButtonClass: "btn btn-secondary",
                    heightAuto: false,
                    });
                }
                });
        } else {
            Swal.fire({
              title: "Error",
              text: "Please, provide correct details!",
              icon: "error",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            });
        }
    },
    microsoft_switch_change() {
        if (this.microsoft_switch) {
            this.microsoft_sender_name = this.microsoft_email
            this.microsoft_username_disable = true
        }
        else {
            this.microsoft_sender_name = ""
            this.microsoft_username_disable = false
        }
    },
  },
  computed: {
        microsoft_username: {
            set(value) {
                this.microsoft_sender_name = value
            },
            get() {
                if (this.microsoft_switch) {
                    return this.microsoft_email
                }
                else {
                    return this.microsoft_sender_name
                }
            }
        },
  }
};
</script>
