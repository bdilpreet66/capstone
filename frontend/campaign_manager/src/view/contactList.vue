<template>
  <div class="d-flex flex-column-fluid">
    <!--begin::Container-->
      <ContactsListTable v-if="showtable"/>
      <ContactsListCreateForm v-if="showform"/>
      <ContactsListInfo v-if="Info"/>
    <!--end::Container-->
  </div>
</template>

<script>
import ContactsListTable from "@/view/contactList/table.vue"
import ContactsListCreateForm from "@/view/contactList/create.vue"
import ContactsListInfo from "@/view/contactList/view.vue"
import store from "@/core/services/store/store.js";

export default {
  name: "ContactList",
  components: {
    ContactsListTable,
    ContactsListCreateForm,
    ContactsListInfo
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
      return store.state.contactListPageControls.table;
    },
    showform() {
      return store.state.contactListPageControls.create;
    },
    Info(){
      return store.state.contactListPageControls.view;
    }
  },
};
</script>