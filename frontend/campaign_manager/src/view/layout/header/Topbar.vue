<template>
  <!-- begin:: Header Topbar -->
  <div class="topbar">

    <!--begin: Quick panel toggle -->
    <KTQuickActions></KTQuickActions>
    <!--end: Quick panel toggle -->

    <!--begin: User Bar -->
    <KTQuickUser></KTQuickUser>
    <!--end: User Bar -->
  </div>
  <!-- end:: Header Topbar -->
</template>

<style lang="scss">
.topbar {
  .dropdown-toggle {
    padding: 0;
    &:hover {
      text-decoration: none;
    }

    &.dropdown-toggle-no-caret {
      &:after {
        content: none;
      }
    }
  }

  .dropdown-menu {
    margin: 0;
    padding: 0;
    outline: none;
    .b-dropdown-text {
      padding: 0;
    }
  }
}
</style>

<script>
import KTQuickUser from "@/view/layout/extras/offcanvas/QuickUser.vue";
import KTQuickActions from "@/view/layout/extras/offcanvas/QuickActions.vue";

export default {
  name: "KTTopbar",
  data() {
    return {};
  },
  components: {
    KTQuickUser,
    KTQuickActions,
  },
  methods: {},
  computed: {
    getLanguageFlag() {
      return this.onLanguageChanged();
    }
  }
};
</script>
