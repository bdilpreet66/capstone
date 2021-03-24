<template>
  <div class="card card-custom">
    <List v-if="currentView==0"></List>
    <Gmail v-if="currentView==1"></Gmail>
    <Outlook v-if="currentView==2"></Outlook>
    <Custom v-if="currentView==3"></Custom>
  </div>
</template>

<script>
import List from "@/view/profile/integrations/list.vue";
import store from "@/core/services/store/store.js";
import Gmail from "@/view/profile/integrations/gmail.vue";
import Outlook from "@/view/profile/integrations/outlook.vue";
import Custom from "@/view/profile/integrations/custom.vue";

export default {
  name: "EmailSettings",
  components: {
    List,
    Gmail,
    Outlook,
    Custom
  },
  data: () => {
    return {
    };
  },
  beforeMount() {
    store.state.integration.view = 0;
  },
  computed: {
    currentView() {
      return store.state.integration.view;
    }
  }
};
</script>
