<template>
  <div class="d-flex flex-column-fluid">
    <!--begin::Container-->
      <TemplatesTable v-if="showtable"/>
      <TemplatesCreateForm v-if="showform"/>
      <TemplatesUpdateForm v-if="showUpdateForm"/>
    <!--end::Container-->
  </div>
</template>

<script>
import TemplatesTable from "@/view/Templates/tables.vue"
import TemplatesCreateForm from "@/view/Templates/create.vue"
import TemplatesUpdateForm from "@/view/Templates/update.vue"
import store from "@/core/services/store/store.js";

export default {
  name: "Templates",
  components: {
    TemplatesTable,
    TemplatesCreateForm,
    TemplatesUpdateForm
  },
  data: () => {
    return {
    };
  },
  beforeMount() {
  },
  methods: {
  },
  computed: {
    showtable() {
      return store.state.TemplatesPageControls.table;
    },
    showform() {
      return store.state.TemplatesPageControls.create;
    },
    showUpdateForm() {
      return store.state.TemplatesPageControls.update;
    },
  },
};
</script>