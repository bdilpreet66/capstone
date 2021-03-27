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
                ref="custom_form"
                v-model="custom_valid"
                lazy-validation
                >
                <v-row class="mx-0 mb-2">
                    <v-text-field
                        v-model="custom_emails_per_day"
                        label="No of emails your email provider allows you to send per day"
                        :rules="[rules.required, rules.emails]"
                        class="form-control form-control-lg form-control-solid"
                        type="number"
                    ></v-text-field>
                </v-row>
            
                <v-row>
                    <v-col class="mx-4">
                        <v-row class="mx-6 my-4">
                            <span class="mt-3 font-weight-medium text--secondary">Recieving emails</span>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                v-model="custom_IMAP_HOST"
                              :rules="[rules.required]"
                                label="IMAP Host"
                                placeholder="imap.host.com"
                                class="form-control form-control-lg form-control-solid"
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                v-model="custom_IMAP_Port"
                              :rules="[rules.required]"
                                label="IMAP Port"
                                class="form-control form-control-lg form-control-solid"
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                          <v-text-field
                              v-model="custom_smtp_email"
                              :rules="[rules.required, rules.email]"
                              class="form-control form-control-lg form-control-solid"
                              label="E-mail*"
                          ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                          <v-text-field
                              v-model="custom_smtp_username"
                              :rules="[rules.required]"
                              label="User Name*"
                              class="form-control form-control-lg form-control-solid"
                          ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                :append-icon="custom_IMAP_show ? 'mdi-eye' : 'mdi-eye-off'"
                                :rules="[rules.required]"
                                :type="custom_IMAP_show ? 'text' : 'password'"
                                label="Password"
                                class="form-control form-control-lg form-control-solid input-group--focused"
                                v-model="custom_IMAP_password"
                                @click:append="custom_IMAP_show = !custom_IMAP_show"
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-select
                                v-model="custom_IMAP_options"
                                :items="custom_OPTIONS"
                                prepend-inner-icon="mdi-earth"
                                class="form-control form-control-lg form-control-solid"
                            ></v-select>
                        </v-row>
                    </v-col>
                    <v-col class="mx-4">
                        <v-row class="mx-6 my-4">
                            <span class="mt-3 font-weight-medium text--secondary">Sending emails</span>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                v-model="custom_SMTP_HOST"
                              :rules="[rules.required]"
                                label="SMTP Host"
                                placeholder="smtp.host.com"
                                class="form-control form-control-lg form-control-solid"
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                v-model="custom_SMTP_Port"
                              :rules="[rules.required]"
                                label="SMTP Port"
                                class="form-control form-control-lg form-control-solid"
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                          <v-text-field
                              v-model="custom_imap_email"
                              :rules="[rules.required, rules.email]"
                              class="form-control form-control-lg form-control-solid"
                              label="E-mail*"
                          ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                          <v-text-field
                              v-model="custom_imap_username"
                              :rules="[rules.required]"
                              label="User Name*"
                              class="form-control form-control-lg form-control-solid"
                          ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-text-field
                                :append-icon="custom_SMTP_show ? 'mdi-eye' : 'mdi-eye-off'"
                                :rules="[rules.required]"
                                :type="custom_SMTP_show ? 'text' : 'password'"
                                label="Password"
                                v-model="custom_SMTP_password"
                                class="form-control form-control-lg form-control-solid input-group--focused"
                                @click:append="custom_SMTP_show = !custom_SMTP_show"
                            ></v-text-field>
                        </v-row>
                        <v-row class="my-4">
                            <v-select
                                v-model="custom_SMTP_options"
                                :items="custom_OPTIONS"
                                prepend-inner-icon="mdi-earth"
                                class="form-control form-control-lg form-control-solid"
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
  name: "Custom",
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

        custom_show: false,
        custom_IMAP_show: false,
        custom_IMAP_password: '',
        custom_IMAP_HOST: '',
        custom_IMAP_Port: 25,
        custom_IMAP_options: 'Enable SSL',
        custom_SMTP_show: false,
        custom_SMTP_password: '',
        custom_SMTP_HOST: '',
        custom_SMTP_Port: 25,
        custom_SMTP_options: 'STARTTLS',
        custom_OPTIONS: ['Enable SSL','STARTTLS'],
        custom_emails_per_day: 300,

        custom_smtp_email: '',
        custom_smtp_username: '',
        custom_imap_email: '',
        custom_imap_username: '',
        custom_switch: false,
        custom_valid: true
    };
  },
  beforeMount(){
      
  },
  methods: {
    changeView(){
          store.state.integration.view = 0;
      },
    Integrate(){
        if(this.$refs.custom_form.validate()){
            var data = {
                'SMTPemail': this.custom_smtp_email,
                'SMTPusername': this.custom_smtp_username,
                'IMAPemail': this.custom_imap_email,
                'IMAPusername': this.custom_imap_username,
                'IMAP_password': this.custom_IMAP_password,
                'IMAP_host': this.custom_IMAP_HOST,
                'IMAP_type': this.custom_IMAP_options,
                'IMAP_port': this.custom_IMAP_Port,
                'smtp_host': this.custom_SMTP_HOST,
                'smtp_port': this.custom_SMTP_Port,
                'smtp_password': this.custom_SMTP_password,
                'smtp_type': this.custom_SMTP_options,
                'emails_per_day': this.custom_emails_per_day
            }
            axios.defaults.baseURL = "http://127.0.0.1:8000/";
            axios.defaults.headers.post["Content-Type"] = "application/json";
            axios.defaults.headers.common["Authorization"] =
                "Token " + Vue.$cookies.get("key");
            axios
                .post("api/user/custom/connect/", data)
                .then(function () {
                    store.state.integration.view = 0;
                })
                .catch(function (error) {
                if (error.response) {
                    Swal.fire({
                    title: "Error",
                    text: "Failed to connect to service!",
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
  },
  computed: {
  }
};
</script>