<template>
  <div class="topbar-item mr-4">
    <div
      class="btn btn-icon btn-sm btn-clean btn-text-dark-75"
      id="kt_quick_user_toggle"
    >
      <span class="svg-icon svg-icon-lg">
        <inline-svg src="media/svg/icons/General/User.svg" />
      </span>
    </div>

    <div
      id="kt_quick_user"
      ref="kt_quick_user"
      class="offcanvas offcanvas-right p-10"
    >
      <!--begin::Header-->
      <div
        class="offcanvas-header d-flex align-items-center justify-content-between pb-5"
      >
        <h3 class="font-weight-bold m-0">
          User Profile
        </h3>
        <a
          href="#"
          class="btn btn-xs btn-icon btn-light btn-hover-primary"
          id="kt_quick_user_close"
        >
          <i class="ki ki-close icon-xs text-muted"></i>
        </a>
      </div>
      <!--end::Header-->

      <!--begin::Content-->
      <perfect-scrollbar
        class="offcanvas-content pr-5 mr-n5 scroll"
        style="max-height: 90vh; position: relative;"
      >
        <!--begin::Header-->
        <div class="d-flex align-items-center mt-5">
          <div class="symbol symbol-100 mr-5">
            <img class="symbol-label" :src="picture" alt="" />
          </div>
          <div class="d-flex flex-column">
            <a
              href="#"
              class="font-weight-bold font-size-h5 text-dark-75 text-hover-primary"
            >
              {{ username }}
            </a>
            <div class="text-muted mt-1">{{ name }}</div>
            <div class="navi mt-2">
              <a href="#" class="navi-item">
                <span class="navi-link p-0 pb-2">
                  <span class="navi-icon mr-1">
                    <span class="svg-icon svg-icon-lg svg-icon-primary">
                      <!--begin::Svg Icon-->
                      <inline-svg
                        src="media/svg/icons/Communication/Mail-notification.svg"
                      />
                      <!--end::Svg Icon-->
                    </span>
                  </span>
                  <a :href="'mailto:'+email" class="navi-text text-muted text-hover-primary">
                    {{ email }}
                  </a>
                </span>
              </a>
            </div>
            <button class="btn btn-light-primary btn-bold" @click="onLogout">
              Sign out
            </button>
          </div>
        </div>
        <!--end::Header-->
        <div class="separator separator-dashed mt-8 mb-5"></div>
        <!--begin::Nav-->
        <div class="navi navi-spacer-x-0 p-0">
          <!--begin::Item-->
          <router-link
            to="/profile"
            @click.native="closeOffcanvas"
            href="#"
            class="navi-item"
          >
            <div class="navi-link">
              <div class="symbol symbol-40 bg-light mr-3">
                <div class="symbol-label">
                  <span class="svg-icon svg-icon-md svg-icon-success">
                    <!--begin::Svg Icon-->
                    <inline-svg
                      src="media/svg/icons/General/Notification2.svg"
                    />
                    <!--end::Svg Icon-->
                  </span>
                </div>
              </div>
              <div class="navi-text">
                <div class="font-weight-bold">My Profile</div>
                <div class="text-muted">
                  Account settings and more
                </div>
              </div>
            </div>
          </router-link>
          <!--end:Item-->
          <!--begin::Item-->
          <router-link
            to="/dashboard"
            @click.native="closeOffcanvas"
            href="#"
            class="navi-item"
          >
            <div class="navi-link">
              <div class="symbol symbol-40 bg-light mr-3">
                <div class="symbol-label">
                  <span class="svg-icon svg-icon-md svg-icon-warning">
                    <!--begin::Svg Icon-->
                    <inline-svg src="media/svg/icons/Shopping/Chart-bar1.svg" />
                    <!--end::Svg Icon-->
                  </span>
                </div>
              </div>
              <div class="navi-text">
                <div class="font-weight-bold">Dashboard</div>
                <div class="text-muted">Overview of your schedules</div>
              </div>
            </div>
          </router-link>
          <!--end:Item-->
        </div>
        <!--end::Nav-->
        <div class="separator separator-dashed my-7"></div>
        <!--begin::Notifications-->
        <div>
          <!--begin:Heading-->
          <h5 class="mb-5">Recent Schedules</h5>
          <!--end:Heading-->
          <template v-for="(item, i) in list">
            <!--begin::Item -->
            <div
              class="d-flex align-items-center rounded p-5 gutter-b"
              v-bind:class="`bg-light-${item.type}`"
              v-bind:key="i"
            >
              <span
                class="svg-icon mr-5"
                v-bind:class="`svg-icon-${item.type}`"
              >
                <span class="svg-icon svg-icon-lg">
                  <!--begin::Svg Icon-->
                  <inline-svg :src="item.svg" />
                  <!--end::Svg Icon-->
                </span>
              </span>
              <div class="d-flex flex-column flex-grow-1 mr-2">
                <a
                  href="#"
                  class="font-weight-normal text-dark-75 text-hover-primary font-size-lg mb-1"
                >
                  {{ item.title }}
                </a>
                <span class="text-muted font-size-sm">
                  {{ item.desc }}
                </span>
              </div>
              <span
                class="font-weight-bolder py-1 font-size-lg"
                v-bind:class="`text-${item.type}`"
              >
                {{ item.alt }}
              </span>
            </div>
            <!--end::Item -->
          </template>
        </div>
        <!--end::Notifications-->
      </perfect-scrollbar>
      <!--end::Content-->
    </div>
  </div>
</template>

<style lang="scss" scoped>
#kt_quick_user {
  overflow: hidden;
}
</style>

<script>
import KTLayoutQuickUser from "@/assets/js/layout/extended/quick-user.js";
import KTOffcanvas from "@/assets/js/components/offcanvas.js";
import Vue from 'vue';
import VueCookies from 'vue-cookies';
Vue.use(VueCookies)
import router from "@/router.js";

export default {
  name: "KTQuickUser",
  data() {
    return {
      list: []
    };
  },
  mounted() {
    // Init Quick User Panel
    KTLayoutQuickUser.init(this.$refs["kt_quick_user"]);
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
    closeOffcanvas() {
      new KTOffcanvas(KTLayoutQuickUser.getElement()).hide();
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
    name() {
      return Vue.$cookies.get("first_name") + " " + Vue.$cookies.get("last_name");
    }
  }
};
</script>
