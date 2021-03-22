<template>
  <div class="card card-custom">
    <!--begin::Header-->
    <div class="card-header py-3">
      <div class="card-title align-items-start flex-column">
        <h3 class="card-label font-weight-bolder text-dark">Email Settings</h3>
        <span class="text-muted font-weight-bold font-size-sm mt-1"
          >Change your email settings</span
        >
      </div>
    </div>
    <!--end::Header-->
    <!--begin::Form-->
      <div class="card-body">
            <div class="row justify-content-center my-20">
                <!--begin: Pricing-->
                <div class="col-md-4 col-xxl-3">
                    <div class="pt-30 pt-md-25 pb-15 px-5 text-center">
                        <!--begin::Icon-->
                        <div class="d-flex flex-center position-relative mb-25">
                            <span class="svg svg-fill-primary opacity-4 position-absolute">
                                <svg width="175" height="200">
                                    <polyline points="87,0 174,50 174,150 87,200 0,150 0,50 87,0"></polyline>
                                </svg>
                            </span>
                            <span class="svg-icon svg-icon-5x svg-icon-primary">
                                <img width="100" src="@/assets/gmail.png" alt="gmail">
                            </span>
                        </div>
                        <!--end::Icon-->
                        <!--begin::Content-->
                        <span class="font-size-h1 d-block d-block font-weight-boldest text-dark-75 py-2">Gmail</span>
                        <h4 class="font-size-h6 d-block d-block font-weight-bold mb-7 text-dark-50">API Integration</h4>
                        <p class="mb-15 d-flex flex-column">
                            <span>Integrate with gmails easy to use mail server api developed by google and used by many all over the world</span>
                        </p>
                        <a href="javascript:;" @click="changeView(1)" class="btn btn-primary text-uppercase font-weight-bolder px-15 py-3">Integrate</a>
                        <!--end::Content-->
                    </div>
                </div>
                <!--end: Pricing-->
                <!--begin: Pricing-->
                <div class="col-md-4 col-xxl-3 border-x-0 border-x-md border-y border-y-md-0">
                    <div class="pt-30 pt-md-25 pb-15 px-5 text-center">
                        <!--begin::Icon-->
                        <div class="d-flex flex-center position-relative mb-25">
                            <span class="svg svg-fill-primary opacity-4 position-absolute">
                                <svg width="175" height="200">
                                    <polyline points="87,0 174,50 174,150 87,200 0,150 0,50 87,0"></polyline>
                                </svg>
                            </span>
                            <span class="svg-icon svg-icon-5x svg-icon-primary">
                                <img width="100" src="@/assets/outlook.png" alt="outlook">
                            </span>
                        </div>
                        <!--end::Icon-->
                        <!--begin::Content-->
                        <span class="font-size-h1 d-block d-block font-weight-boldest text-dark-75 py-2">Outlook</span>
                        <h4 class="font-size-h6 d-block d-block font-weight-bold mb-7 text-dark-50">SMTP/IMAP Integration</h4>
                        <p class="mb-15 d-flex flex-column">
                            <span>Integrate with outlooks highly advanced and easily managable SMTP and IMAP Servers to send emails</span>
                        </p>
                        <a href="javascript:;" @click="changeView(2)" class="btn btn-primary text-uppercase font-weight-bolder px-15 py-3">Integrate</a>
                        <!--end::Content-->
                    </div>
                </div>
                <!--end: Pricing-->
                <!--begin: Pricing-->
                <div class="col-md-4 col-xxl-3">
                    <div class="pt-30 pt-md-25 pb-15 px-5 text-center">
                        <!--begin::Icon-->
                        <div class="d-flex flex-center position-relative mb-25">
                            <span class="svg svg-fill-primary opacity-4 position-absolute">
                                <svg width="175" height="200">
                                    <polyline points="87,0 174,50 174,150 87,200 0,150 0,50 87,0"></polyline>
                                </svg>
                            </span>
                            <span class="svg-icon svg-icon-5x svg-icon-primary">
                                <img width="130" src="@/assets/custom.png" alt="custom">
                            </span>
                        </div>
                        <!--end::Icon-->
                        <!--begin::Content-->
                        <span class="font-size-h1 d-block d-block font-weight-boldest text-dark-75 py-2">Custom</span>
                        <h4 class="font-size-h6 d-block d-block font-weight-bold mb-7 text-dark-50">SMTP/IMAP Integrations</h4>
                        <p class="mb-15 d-flex flex-column">
                            <span>ALLow you to connect with a wide variety of SMTP and IMAP Servers providing support for millions of Services.</span>
                        </p>
                        <a href="javascript:;" @click="changeView(3)" class="btn btn-primary text-uppercase font-weight-bolder px-15 py-3">Integrate</a>
                        <!--end::Content-->
                    </div>
                </div>
                <!--end: Pricing-->
            </div>
        </div>
    <!--end::Form-->
  </div>
</template>

<script>
import store from "@/core/services/store/store.js";

export default {
  name: "List",
  data: () => {
    return {
    };
  },
  methods: {
      changeView(number){
          store.state.integration.view = number;
      }
  }
};
</script>
