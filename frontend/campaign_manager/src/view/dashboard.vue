<template>
    <div
        id="kt_content"
        class="content d-flex flex-column flex-column-fluid"
    >
    <!--begin::Entry-->
    <div class="d-flex flex-column-fluid">
        <!--begin::Container-->
        <div class="container">
            <div class="row">
                <div class="col-xl-4 col-lg-4 col-md-4">
                    <div class="card card-custom gutter-b card-shadowless card-stretch" style="background-color:rgb(23, 23, 41)">
                        <!--begin::Header-->
                        <div class="card-header border-0">
                            <h3 class="card-title font-weight-bolder text-success">Welcome to your dashboard</h3>
                        </div>
                        <!--end::Header-->
                        <!--begin::Body-->
                        <div class="card-body pt-2">
                            <!--begin::Item-->
                            <p class="text-muted">Here you will find an overview of your most recent Campaigns and some other stuff</p>
                            <!--end::Item-->
                        </div>
                        <!--end::Body-->
                    </div>
                </div>
                <div class="col-xl-8 col-lg-8 col-md-8">
                    <!--begin::Charts Widget 2-->
                    <div class="card card-custom bg-gray-100 gutter-b card-stretch card-shadowless">
                        <div class="card-header flex-wrap py-5">
                            <div class="card-title">
                                <h3 class="card-label">Campaigns
                                </h3>
                            </div>
                            <div class="card-toolbar">
                                <!--begin::Button-->
                                <router-link to="/campaigns" v-slot="{ href, navigate }">
                                <a
                                    :href="href"
                                    class="btn btn-primary font-weight-bolder"
                                    @click="navigate"
                                    >View All
                                </a>
                                </router-link>
                                <!--end::Button-->
                            </div>
                        </div>
                        <div class="card-body">
                            <!--begin::Table-->
                            <div class="table-responsive">
                                <table class="table table-borderless mb-0">
                                    <tbody>
                                        <!--begin::Item-->
                                        <tr>
                                            <td class="font-size-lg font-weight-bolder text-dark-75 align-middle w-200px pb-6">
                                                <h6 class="card-label">fsdf
                                                    <div class="pt-2 font-size-sm">Email:
                                                        <spam class="text-muted">fsdf</spam>
                                                    </div>
                                                </h6>
                                            </td>
                                            <td class="font-weight-bold text-right align-middle pb-6">
                                                <h6 class="card-label">fsfsdf
                                                    <div class="text-muted pt-2 font-size-sm">dsd</div>
                                                </h6>
                                            </td>
                                            <td class="font-weight-bold text-right align-middle pb-12">
                                                <span class="label label-lg font-weight-bold label-light-success label-inline">hfg</span></td>
                                        </tr>
                                        <!--end::Item-->
                                    </tbody>
                                </table>
                            </div>
                            <!--end::Table-->
                        </div>
                    </div>
                    <!--end::Charts Widget 2-->
                </div>
            </div>
        </div>
        <!--end::Container-->
    </div>
    <!--end::Entry-->
    <!--begin::Entry-->
    <div class="d-flex flex-column-fluid">
        <!--begin::Container-->
        <div class="container">
            <div class="row">
                <div class="col-6">
                    <!--begin::Charts Widget 2-->
                    <div class="card card-custom bg-gray-100 gutter-b card-stretch card-shadowless">
                        <div class="card-header flex-wrap py-5">
                            <div class="card-title">
                                <h3 class="card-label">Contacts
                                </h3>
                            </div>
                            <div class="card-toolbar">
                                <!--begin::Button-->
                                <router-link to="/contacts" v-slot="{ href, navigate }">
                                <a
                                    :href="href"
                                    class="btn btn-primary font-weight-bolder"
                                    @click="navigate"
                                    >View All
                                </a>
                                </router-link>
                                <!--end::Button-->
                            </div>
                        </div>
                        <div class="card-body">
                            <!--begin::Table-->
                            <div class="table-responsive">
                                <table class="table table-borderless mb-0">
                                    <tbody>
                                        <!--begin::Item-->
                                        <tr>
                                            <td class="font-size-lg font-weight-bolder text-dark-75 align-middle w-200px pb-6">
                                                <h6 class="card-label">fsdf
                                                    <div class="pt-2 font-size-sm">Email:
                                                        <spam class="text-muted">fsdf</spam>
                                                    </div>
                                                </h6>
                                            </td>
                                            <td class="font-weight-bold text-right align-middle pb-6">
                                                <h6 class="card-label">fsfsdf
                                                    <div class="text-muted pt-2 font-size-sm">dsd</div>
                                                </h6>
                                            </td>
                                            <td class="font-weight-bold text-right align-middle pb-12">
                                                <span class="label label-lg font-weight-bold label-light-success label-inline">hfg</span></td>
                                        </tr>
                                        <!--end::Item-->
                                    </tbody>
                                </table>
                            </div>
                            <!--end::Table-->
                        </div>
                    </div>
                    <!--end::Charts Widget 2-->
                </div>
                <div class="col-6">
                    <!--begin::Charts Widget 2-->
                    <div class="card card-custom bg-gray-100 gutter-b card-stretch card-shadowless">
                        <div class="card-header flex-wrap py-5">
                            <div class="card-title">
                                <h3 class="card-label">Templates
                                </h3>
                            </div>
                            <div class="card-toolbar">
                                <!--begin::Button-->
                                <router-link to="/templates" v-slot="{ href, navigate }">
                                <a
                                    :href="href"
                                    class="btn btn-primary font-weight-bolder"
                                    @click="navigate"
                                    >View All
                                </a>
                                </router-link>
                                <!--end::Button-->
                            </div>
                        </div>
                        <div class="card-body">
                            <!--begin::Table-->
                            <div class="table-responsive">
                                <table class="table table-borderless mb-0">
                                    <tbody>
                                        <!--begin::Item-->
                                        <tr>
                                            <td class="font-size-lg font-weight-bolder text-dark-75 align-middle w-200px pb-6">
                                                <h6 class="card-label">fsdf
                                                    <div class="pt-2 font-size-sm">Email:
                                                        <spam class="text-muted">fsdf</spam>
                                                    </div>
                                                </h6>
                                            </td>
                                            <td class="font-weight-bold text-right align-middle pb-6">
                                                <h6 class="card-label">fsfsdf
                                                    <div class="text-muted pt-2 font-size-sm">dsd</div>
                                                </h6>
                                            </td>
                                            <td class="font-weight-bold text-right align-middle pb-12">
                                                <span class="label label-lg font-weight-bold label-light-success label-inline">hfg</span></td>
                                        </tr>
                                        <!--end::Item-->
                                    </tbody>
                                </table>
                            </div>
                            <!--end::Table-->
                        </div>
                    </div>
                    <!--end::Charts Widget 2-->
                </div>
            </div>
        </div>
        <!--end::Container-->
    </div>
    <!--end::Entry-->
    </div>
</template>

<script>

export default {
  name: "Dashboard",
  beforeMount() {
  },
  methods: {
  },
  computed: {
  },
};
</script>