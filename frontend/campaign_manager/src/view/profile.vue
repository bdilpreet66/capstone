<template>
  <div class="d-flex flex-row m-12">
    <div
      class="flex-row-auto offcanvas-mobile w-300px w-xl-350px mt-6"
      id="kt_profile_aside"
    >
      <div class="card card-custom card-stretch">
        <div class="card-body pt-4">
          <div class="d-flex align-items-center">
            <div
              class="symbol symbol-60 symbol-xxl-100 mr-5 align-self-start align-self-xxl-center"
            >
              <div
                class="symbol-label"
                :style="{
                  backgroundImage: `url(`+picture+`)`
                }"
              ></div>
            </div>
            <div>
              <a
                class="font-weight-bolder font-size-h5 text-dark-75 text-hover-primary"
                >{{ username }}</a
              >
              <div class="text-muted">{{ name }}</div>
              <div class="mt-2">
                <button class="btn btn-light-primary btn-bold" @click="onLogout">
                Sign out
                </button>
              </div>
            </div>
          </div>
          <!--end::User-->
          <!--begin::Contact-->
          <div class="py-9">
            <div class="d-flex align-items-center justify-content-between mb-2">
              <span class="font-weight-bold mr-2">Email:</span>
              <a :href="'mailto:'+email" class="text-muted text-hover-primary" target="_blank">{{ email }}</a>
            </div>
            <div class="d-flex align-items-center justify-content-between mb-2">
              <span class="font-weight-bold mr-2">Phone:</span>
              <span class="text-muted">{{ mob }}</span>
            </div>
            <div class="d-flex align-items-center justify-content-between">
              <span class="font-weight-bold mr-2">Company Name:</span>
              <span class="text-muted">{{ cname }}</span>
            </div>
            <div class="d-flex align-items-center justify-content-between">
              <span class="font-weight-bold mr-2">Website:</span>
              <a class="text-muted">{{ website }}</a>
            </div>
          </div>
          <!--end::Contact-->
          <!--begin::Nav-->
          <div
            class="navi navi-bold navi-hover navi-active navi-link-rounded"
            role="tablist"
          >
            <div class="navi-item mb-2">
              <a
                class="navi-link py-4 active"
                @click="setActiveTab"
                style="cursor:pointer"
                data-tab="0"
                data-toggle="tab"
                role="tab"
                aria-selected="false"
              >
                <span class="navi-icon mr-2">
                  <span class="svg-icon">
                    <inline-svg src="media/svg/icons/General/User.svg" />
                  </span>
                </span>
                <span class="navi-text font-size-lg">Personal Information</span>
              </a>
            </div>
            <div class="navi-item mb-2">
              <a
                class="navi-link py-4"
                @click="setActiveTab"
                style="cursor:pointer"
                data-tab="1"
                data-toggle="tab"
                role="tab"
                aria-selected="false"
              >
                <span class="navi-icon mr-2">
                  <span class="svg-icon">
                    <inline-svg src="media/svg/icons/Code/Compiling.svg" />
                  </span>
                </span>
                <span class="navi-text font-size-lg">Security</span>
              </a>
            </div>
            <div class="navi-item mb-2">
              <a
                class="navi-link py-4"
                @click="setActiveTab"
                style="cursor:pointer"
                data-tab="2"
                data-toggle="tab"
                role="tab"
                aria-selected="false"
              >
                <span class="navi-icon mr-2">
                  <span class="svg-icon">
                    <inline-svg
                      src="media/svg/icons/Communication/Shield-user.svg"
                    />
                  </span>
                </span>
                <span class="navi-text font-size-lg">Change Passwors</span>
              </a>
            </div>
            <div class="navi-item mb-2">
              <a
                class="navi-link py-4"
                @click="setActiveTab"
                style="cursor:pointer"
                data-tab="3"
                data-toggle="tab"
                role="tab"
                aria-selected="false"
              >
                <span class="navi-icon mr-2">
                  <span class="svg-icon">
                    <inline-svg
                      src="media/svg/icons/Communication/Mail-opened.svg"
                    />
                  </span>
                </span>
                <span class="navi-text font-size-lg">Email settings</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!--begin::Content-->
    <div class="flex-row-fluid ml-lg-8">
      <b-tabs class="hide-tabs" v-model="tabIndex">
        <b-tab active>
          <KTPersonalInformation></KTPersonalInformation>
        </b-tab>

        <b-tab>
          <KTAccountInformation></KTAccountInformation>
        </b-tab>

        <b-tab>
          <KTChangePassword></KTChangePassword>
        </b-tab>

        <b-tab>
          <KTEmailSettings></KTEmailSettings>
        </b-tab>
      </b-tabs>
    </div>
    <!--end::Content-->
  </div>
</template>

<script>
import KTPersonalInformation from "@/view/profile/PersonalInformation";
import KTAccountInformation from "@/view/profile/AccountInformation";
import KTChangePassword from "@/view/profile/ChangePassword";
import KTEmailSettings from "@/view/profile/EmailSettings";
import router from "@/router.js";
import Vue from 'vue';
import VueCookies from 'vue-cookies';
Vue.use(VueCookies)
// import store from "@/core/services/store/store.js";

export default {
  name: "Profile",
  components: {
    KTPersonalInformation,
    KTAccountInformation,
    KTChangePassword,
    KTEmailSettings
  },
  data: () => {
    return {
      tabIndex: 0
    };
  },
  beforeMount() {
  },
  methods: {
    onLogout() {
      Vue.$cookies.remove("key");
      Vue.$cookies.remove("remember_key");
      Vue.$cookies.remove("logo");
      Vue.$cookies.remove("company_site");
      Vue.$cookies.remove("contact_number");
      Vue.$cookies.remove("company_name");
      Vue.$cookies.remove("username");
      Vue.$cookies.remove("email");
      Vue.$cookies.remove("first_name");
      Vue.$cookies.remove("last_name");
      router.replace({ name: "login" });
    },

    /**
     * Set current active on click
     * @param event
     */
    setActiveTab(event) {
      let target = event.target;
      if (!event.target.classList.contains("navi-link")) {
        target = event.target.closest(".navi-link");
      }

      const tab = target.closest('[role="tablist"]');
      const links = tab.querySelectorAll(".navi-link");
      // remove active tab links
      for (let i = 0; i < links.length; i++) {
        links[i].classList.remove("active");
      }

      // set clicked tab index to bootstrap tab
      this.tabIndex = parseInt(target.getAttribute("data-tab"));

      // set current active tab
      target.classList.add("active");
    }
  },
  computed: {
    picture() {
      return Vue.$cookies.get("logo");
    },
    username() {
      return Vue.$cookies.get("username");
    }, 
    email() {
      return Vue.$cookies.get("email");
    },
    mob() {
      return Vue.$cookies.get("contact_number");
    },
    cname() {
      return Vue.$cookies.get("company_name");
    },
    website() {
      return Vue.$cookies.get("company_site");
    },    
    name() {
      return Vue.$cookies.get("first_name") + " " + Vue.$cookies.get("last_name");
    }
  }
};
</script>