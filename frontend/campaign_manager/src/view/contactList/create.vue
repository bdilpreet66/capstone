<template>
  <div class="d-flex flex-column-fluid mt-12">
    <!--begin::Container-->
    <div class="container">
      <!--begin::Card-->
      <div class="card card-custom">
        <div class="card-header flex-wrap py-5">
          <div class="card-title">
            <h3 class="card-label">
              New Contact List
              <div class="text-muted pt-2 font-size-sm">Upload a new contact list</div>
            </h3>
          </div>
          <div class="card-toolbar">
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
            <div class="form-group row align-items-center tab-content mt-5">
                <a href="javascript:;" id="Csv_loader" class="col-lg-12 btn btn-sm font-weight-bolder btn-light-primary">
                    <div class="dropzone dropzone-default dz-clickable">
                        <div class="dropzone-msg dz-message needsclick">
                            <img height="100" src="@/assets/CSV.png" alt="CSV LOGO" />
                            <h3 id="name" class="dropzone-msg-title mt-3">Upload a new List</h3>
                            <span id="info" class="dropzone-msg-desc">You can click here or drag you csv file in this area to upload you contacts list</span>
                        </div>
                    </div>
                </a>
                <input id="clickInput" type="file" hidden/>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >List Name</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                    <input
                        v-model="name"
                        type="text"
                        class="form-control form-control-lg form-control-solid"
                        placeholder="New List"
                    />
                    </div>
                </div>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >List Reference</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                    <input
                        v-model="ref"
                        type="text"
                        class="form-control form-control-lg form-control-solid"
                        placeholder="List Reference"
                    />
            </div>
                </div>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >List Description</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                        <input
                            v-model="desc"
                            type="text"
                            class="form-control form-control-lg form-control-solid"
                            placeholder="Description"
                        />
                    </div>
                </div>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >Email Field</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                        <input
                            v-model="emailField"
                            type="text"
                            class="form-control form-control-lg form-control-solid"
                            placeholder="email"
                        />
                    </div>
                </div>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >First Name Field</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                        <input
                            v-model="ffield"
                            type="text"
                            class="form-control form-control-lg form-control-solid"
                            placeholder="Description"
                        />
                    </div>
                </div>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >Last Name Field</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                        <input
                            v-model="lfield"
                            type="text"
                            class="form-control form-control-lg form-control-solid"
                            placeholder="Description"
                        />
                    </div>
                </div>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >Contact Ref Field</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                        <input
                            v-model="rfield"
                            type="text"
                            class="form-control form-control-lg form-control-solid"
                            placeholder="Description"
                        />
                    </div>
                </div>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >Description Field</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                        <input
                            v-model="dfield"
                            type="text"
                            class="form-control form-control-lg form-control-solid"
                            placeholder="Description"
                        />
                    </div>
                </div>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >Address Field</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                        <input
                            v-model="afield"
                            type="text"
                            class="form-control form-control-lg form-control-solid"
                            placeholder="Description"
                        />
                    </div>
                </div>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >Bank Info Field</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                        <input
                            v-model="bfield"
                            type="text"
                            class="form-control form-control-lg form-control-solid"
                            placeholder="Description"
                        />
                    </div>
                </div>
            </div>
            <div v-if="hasFile" class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label text-right"
                    >Contact info field</label
                >
                <div class="col-lg-9 col-xl-6">
                    <div class="input-group input-group-lg input-group-solid">
                        <input
                            v-model="pfield"
                            type="text"
                            class="form-control form-control-lg form-control-solid"
                            placeholder="Description"
                        />
                    </div>
                </div>
            </div>
            <div v-if="hasFile" class="modal-footer">
                <div class="row">
                    <button id="submit" @click="submitFile" type="button" style="margin-left:5px;" class="btn btn-success font-weight-bold ">Create List</button>
                </div>
            </div>
        </div>
      </div>
      <!--end::Card-->
    </div>
    <!--end::Container-->
  </div>
</template>

<script>
import store from "@/core/services/store/store.js";
import Swal from "sweetalert2";
import axios from "axios";
import Vue from 'vue';
import VueCookies from 'vue-cookies';
Vue.use(VueCookies)

export default {
  name: "ContactsListCreateForm",
  data: () => {
    return {
        emailField: "",
        name: "",
        ref: "",
        desc: "",
        hasFile: false,
        file: "",
        ffield: "",
        lfield: "",
        rfield: "",
        dfield: "",
        afield: "",
        bfield: "",
        pfield: ""
    };
  },
  mounted() {
      const dropArea = document.getElementById("Csv_loader")

      const input = document.getElementById("clickInput")

      dropArea.addEventListener("click", () => {
          input.click();
      })

      input.addEventListener("change", (event) => {
          if (event.target.files[0].name.split(".")[1] == "csv"){
            this.hasFile = true;
            this.file = event.target.files[0];
            document.getElementById("name").innerHTML = this.file.name;
            document.getElementById("info").innerHTML = "<h4>Size: "+bytesToSize(this.file.size)+"<br>Type: "+this.file.type+"</h4>";
          } else {
            Swal.fire({
                title: "Error",
                text: "The file doesn't have csv format. Please input a csv file",
                icon: "error",
                confirmButtonClass: "btn btn-secondary",
                heightAuto: false,
            });
          }
          dropArea.classList.remove("active")
      })

      dropArea.addEventListener("dragover",(event)=>{
          event.preventDefault();
          dropArea.classList.add("active")
      })
      
      dropArea.addEventListener("dragleave",()=>{
          dropArea.classList.remove("active")
      })
      
      dropArea.addEventListener("drop",(event)=>{
          event.preventDefault();
          if (event.dataTransfer.files[0].name.split(".")[1] == "csv"){
            this.file = event.dataTransfer.files[0];
            document.getElementById("name").innerHTML = this.file.name;
            document.getElementById("info").innerHTML = "<h4>Size: "+bytesToSize(this.file.size)+"<br>Type: "+this.file.type+"</h4>";
            this.hasFile = true;
          } else {
            Swal.fire({
                title: "Error",
                text: "The file doesn't have csv format. Please input a csv file",
                icon: "error",
                confirmButtonClass: "btn btn-secondary",
                heightAuto: false,
            });
          }
          dropArea.classList.remove("active")
      })
      
      function bytesToSize(bytes) {
        var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
        if (bytes == 0) return '0 Byte';
        var i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
        return Math.round(bytes / Math.pow(1024, i), 2) + ' ' + sizes[i];
        }
  },
  methods: {
    submitFile(){
        if(this.emailField != "" && this.name != "" && this.ref != ""){
            let data = new FormData();
            data.append('file', this.file, this.file.fileName);
            data.append('email', this.emailField);
            data.append('name', this.name);
            data.append('ref', this.ref);
            data.append('desc', this.desc);
            data.append('ffield',this.ffield);
            data.append('lfield',this.lfield);
            data.append('rfield',this.rfield);
            data.append('dfield',this.dfield);
            data.append('afield',this.afield);
            data.append('bfield',this.bfield);
            data.append('pfield',this.pfield);            axios.defaults.baseURL = "http://127.0.0.1:8000/";
            axios.defaults.headers.post["Content-Type"] = "application/json";
                axios.defaults.headers.common["Authorization"] =
                    "Token " + Vue.$cookies.get("key");
            axios
                .post("api/contact/Createlist/", data,{headers: {
                    'accept': 'application/json',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Content-Type': `multipart/form-data; boundary=${data._boundary}`,
                }})
                .then(function () {
                    store.state.contactListPageControls.table = true;
                    store.state.contactListPageControls.create = false;
                    Swal.fire({
                    title: "Success",
                    text: "Uploaded Imaage to server.",
                    icon: "success",
                    confirmButtonClass: "btn btn-secondary",
                    heightAuto: false,
                    })
                })
                .catch(function (error) {
                if (error.response) {
                    Swal.fire({
                    title: "Error",
                    text: "Failed to upload CSV to server!",
                    icon: "error",
                    confirmButtonClass: "btn btn-secondary",
                    heightAuto: false,
                    });
                }
                });
        } else {
            Swal.fire({
                title: "",
                text: "Email field, List Name and referece are required field",
                icon: "error",
                confirmButtonClass: "btn btn-secondary",
                heightAuto: false,
            });
        }
    },
    close() {
      store.state.contactListPageControls.table = true;
      store.state.contactListPageControls.create = false;
    },
  },
  computed: {},
};
</script>