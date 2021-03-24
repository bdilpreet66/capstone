<template>
  <div class="d-flex flex-column-fluid">
    <!--begin::Container-->
    <div class="container">
          <form
            class="form"
            id="create_item_form"
            novalidate="novalidate"
            style="margin: 25px"
          >
      <!--begin::Card-->
      <div class="card card-custom">
        <div class="card-header flex-wrap py-5">
          <div class="card-title">
            <h3 class="card-label">
              New Template
              <div class="text-muted pt-2 font-size-sm">Add new Email Template</div>
            </h3>
          </div>
          <div class="card-toolbar">
            <!--begin::Button-->
            <button
                type="submit"
                class="btn btn-success font-weight-bolder mx-3"
              >Submit</button
            >
            <!--end::Button-->
            <!--begin::Button-->
            <a
              href="javascript:;"
              @click="close()"
              class="btn btn-primary font-weight-bolder"
              >Close</a
            >
            <!--end::Button-->
          </div>
        </div>
        <div class="card-body">
            <div class="form-group row">
              <div class="col-lg-6">
                <label>Name</label>
                <input
                  type="text"
                  class="form-control"
                  name="name"
                  placeholder="New Email Template"
                />
                <span class="form-text text-muted"
                  >Please enter name for your template</span
                >
              </div>
            </div>
            <div class="form-group row">
              <div class="col-lg-12">
                <label>Subject</label>
                <input
                  type="text"
                  class="form-control"
                  name="subject"
                  placeholder="New Marketing Campaign"
                />
                <span class="form-text text-muted"
                  >Please enter subject for your Template</span
                >
              </div>
            </div>
            <div class="form-group row">
              <div class="col-lg-12">
                  <editor
                    v-model="editorData"
                    api-key="5m1k2j8b2mllw5ubytknqdgtm2vd7du2jzjdeqf50hvpqcf7"
                    :init="{
                        height: 450,
                        paste_data_images: true,
                        plugins: [
                        'advlist autolink lists link image charmap preview anchor',
                        'searchreplace visualblocks code fullscreen',
                        'insertdatetime media table code help wordcount'
                        ],
                        toolbar:
                        'undo redo | formatselect | bold italic underline forecolor  backcolor | \
                        alignleft aligncenter alignright alignjustify | \
                        bullist numlist outdent indent | removeformat ',
                    }"
                  />
              </div>
            </div>
            <div class="form-group row text-center">
              <div class="col-lg-12">
                  <div class="btn-group" role="group">
                      <button type="button" class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3" v-clipboard:copy="'{link}'"><i class="la la-copy"></i>link</button>
                      <button type="button" class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3" v-clipboard:copy="'{first_name}'"><i class="la la-copy"></i>First Name</button>
                      <button type="button" class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3" v-clipboard:copy="'{last_name}'"><i class="la la-copy"></i>Last Name</button>
                      <button type="button" class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3" v-clipboard:copy="'{address}'"><i class="la la-copy"></i>Address</button>
                      <button type="button" class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3" v-clipboard:copy="'{email}'"><i class="la la-copy"></i>Email</button>
                      <button type="button" class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3" v-clipboard:copy="'{bank}'"><i class="la la-copy"></i>Bank details</button>
                      <button type="button" class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3" v-clipboard:copy="'{contact}'"><i class="la la-copy"></i>Contact</button>
                  </div>
              </div>
            </div>
        </div>
      </div>
      <!--end::Card-->
          </form>
    </div>
    <!--end::Container-->
  </div>
</template>

<script>
import formValidation from "@/assets/plugins/formvalidation/dist/es6/core/Core";

// FormValidation plugins
import Trigger from "@/assets/plugins/formvalidation/dist/es6/plugins/Trigger";
import Bootstrap from "@/assets/plugins/formvalidation/dist/es6/plugins/Bootstrap";
import SubmitButton from "@/assets/plugins/formvalidation/dist/es6/plugins/SubmitButton";

import KTUtil from "@/assets/js/components/util";
import store from "@/core/services/store/store.js";
import Swal from "sweetalert2";
import Editor from '@tinymce/tinymce-vue';
import axios from "axios";
import Vue from 'vue';
import VueCookies from 'vue-cookies';
import VueClipboard from 'vue-clipboard2'
Vue.use(VueCookies)
Vue.use(VueClipboard)

export default {
  name: "TemplatesCreateForm",
   components: {
     'editor': Editor // <- Important part
   },
  data: () => {
    return {
      message:""
    };
  },
  mounted() {
    const form = KTUtil.getById("create_item_form");

    this.fv = formValidation(form, {
      fields: {
        name: {
          validators: {
            notEmpty: {
              message: "reference is required",
            },
          },
        },
        subject: {
          validators: {
            notEmpty: {
              message: "Email is required",
            },
          },
        },
      },
      plugins: {
        trigger: new Trigger(),
        submitButton: new SubmitButton(),
        bootstrap: new Bootstrap(),
      },
    });

    this.fv.on("core.form.valid", () => {
        var form = KTUtil.getById("create_item_form")
        var data = []
        for(var i=0; i<form.length;i++){
            data.push(form[i].value)
        }
        data = {
            name: data[1],
            subject: data[2],
            message: this.message
        };
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
      axios.defaults.headers.common["Authorization"] =
        "Token " + Vue.$cookies.get("key");
      axios
        .post("api/campaign/template/manage/", data)
        .then(function () {
            store.state.TemplatesPageControls.table = true;
            store.state.TemplatesPageControls.create = false;
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              title: "Error",
              text: "Failed to create new user",
              icon: "error",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            });
          }
        });
    });

    this.fv.on("core.form.invalid", () => {
      Swal.fire({
        title: "Error",
        text: "Please, provide correct data!",
        icon: "error",
        confirmButtonClass: "btn btn-secondary",
        heightAuto: false,
      });
    });
  },
  methods: {
    close() {
      store.state.TemplatesPageControls.table = true;
      store.state.TemplatesPageControls.create = false;
    },
  },
  computed: {
    editorData: {
        set(editorData){
            this.message = editorData;
        },
        get(){
            return this.message;
        }
    },
  },
};
</script>