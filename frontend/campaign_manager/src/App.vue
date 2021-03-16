<template>
  <div class="d-flex flex-column flex-root">
  <div id="screen" style="height:100vh; width:100vw; background-color:black; position: absolute; z-index:999; visibility:hidden">
    <video autoplay style="heigth:100%; width:100%;"></video>
  </div>
    <!-- begin:: Header Mobile -->
      <KTHeaderMobile v-if="['login'].indexOf($route.name) == -1"></KTHeaderMobile>

      <div class="d-flex flex-row flex-column-fluid page">
        <div id="kt_wrapper" class="d-flex flex-column flex-row-fluid wrapper">
          <!-- begin:: Header -->
          <KTHeader v-if="['login'].indexOf($route.name) == -1"></KTHeader>
          <!-- end:: Header -->
          <router-view></router-view>
          <KTAside v-if="['login'].indexOf($route.name) == -1"></KTAside>
        </div>
      </div>
      <KTFooter v-if="['login'].indexOf($route.name) == -1"></KTFooter>
  </div>
</template>

<style lang="scss">
// 3rd party plugins css
@import "~bootstrap-vue/dist/bootstrap-vue.css";
@import "~perfect-scrollbar/css/perfect-scrollbar.css";
@import "~socicon/css/socicon.css";
@import "~animate.css";
@import "~@fortawesome/fontawesome-free/css/all.css";
@import "~line-awesome/dist/line-awesome/css/line-awesome.css";
@import "assets/plugins/flaticon/flaticon.css";
@import "assets/plugins/flaticon2/flaticon.css";
@import "assets/plugins/keenthemes-icons/font/ki.css";

// Main demo style scss
@import "assets/sass/style.vue";

// Check documentation for RTL css
// Update HTML with RTL attribute at public/index.html
/*@import "assets/css/style.vue.rtl";*/
</style>

<script>
import { OVERRIDE_LAYOUT_CONFIG } from "@/core/services/store/config.module";
import KTHeader from "@/view/layout/header/Header.vue";
import KTHeaderMobile from "@/view/layout/header/HeaderMobile.vue";
import KTFooter from "@/view/layout/footer/Footer.vue";
import KTAside from "@/view/layout/aside/Aside.vue";

export default {
  name: "Vue",
  components: {
    KTAside,
    KTHeader,
    KTHeaderMobile,
    KTFooter,
  },
  mounted() {
    this.$store.dispatch(OVERRIDE_LAYOUT_CONFIG);
  },
  methods: {
    footerLayout(type) {
      return this.layoutConfig("footer.layout") === type;
    },
  },
  computed: {
    asideEnabled() {
      return true;
    },
    toolbarDisplay() {
      // return !!this.layoutConfig("toolbar.display");
      return true;
    },
    subheaderDisplay() {
      return !!this.layoutConfig("subheader.display");
    },
  },
};
</script>
