<template>
    <div
        id="kt_content"
        class="content d-flex flex-column flex-column-fluid"
    >
    <CampaignList v-if="showtable"></CampaignList>
    <Reports v-if="showReport"></Reports>
    </div>
</template>

<script>
import Reports from "@/view/campaigns/view.vue";
import CampaignList from "@/view/campaigns/list.vue";
import store from "@/core/services/store/store.js";

export default {
  name: "Campaign",
  components: {
    Reports,
    CampaignList
  },
  beforeMount() {
  },
  methods: {
  },
  computed: {
    showtable() {
      return store.state.campaign.table;
    },
    showReport() {
      return store.state.campaign.reports;
    },
  },
};
</script>