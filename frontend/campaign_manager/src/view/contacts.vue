<template>
  <div class="d-flex flex-column-fluid">
    <!--begin::Container-->
      <ContactsTable v-if="showtable"/>
      <ContactsCreateForm v-if="showform"/>
      <ContactsUpdateForm v-if="showUpdateForm"/>
    <!--end::Container-->
  </div>
</template>

<script>
import ContactsTable from "@/view/contacts/tables.vue"
import ContactsCreateForm from "@/view/contacts/create.vue"
import ContactsUpdateForm from "@/view/contacts/update.vue"
import store from "@/core/services/store/store.js";

export default {
  name: "Contacts",
  components: {
    ContactsTable,
    ContactsCreateForm,
    ContactsUpdateForm
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
      return store.state.contactsPageControls.table;
    },
    showform() {
      return store.state.contactsPageControls.create;
    },
    showUpdateForm() {
      return store.state.contactsPageControls.update;
    },
  },
};
</script>