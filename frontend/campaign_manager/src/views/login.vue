<template>
  <div
  class="Login"
  >
      <v-container
      align="center"
      justify="space-around"
      fluid
      class="mb-10"
    >
      <v-row
        align="center"
        justify="space-around"
        min-height: 
      >
        <v-col class="hidden-xs-only" cols="1">
        </v-col>
        <v-col class="hidden-xs-only" cols="4">
          <blockquote class="blockquote"><h1 class="font-weight-bold">Welcome to your secret weapon in marketing</h1></blockquote>
          <blockquote class="blockquote">Easy email marketing for busy teams and people that need to send emails and generate sales and responses. Email marketing is the best.</blockquote>
        </v-col>
        <v-col>
          <v-card
            class="mx-auto"
            max-width="500"
            outlined
          >
            <v-form id="rform" style="display:none" ref="regform">
              <v-container>
                <v-row
                  cols="12"
                  md="4"
                >
                  <v-col>
                    <v-text-field
                      v-model="username"
                      :rules="[rules.required]"
                      label="username"
                      required
                      outlined
                      clearable
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row
                  cols="12"
                  md="4"
                >
                  <v-col>
                    <v-text-field
                      v-model="Email"
                      :rules="[rules.required,rules.emailMatch]"
                      label="Email"
                      required
                      outlined
                      clearable
                    ></v-text-field>
                  </v-col>
                </v-row>
                
                <v-row
                    cols="12"
                    md="4"
                  >
                 
                  <v-col>
                   <v-text-field
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Normal with hint text"
            hint="At least 8 characters"
            counter
            outlined
            @click:append="show1 = !show1"
          ></v-text-field>
                    
                  </v-col>
                </v-row>
                <v-row
                    cols="12"
                    md="4"
                  >
                 
                  <v-col>
                    <v-text-field
            v-model="cpassword"
            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show2 ? 'text' : 'password'"
            name="input-10-1"
            label="Normal with hint text"
            hint="At least 8 characters"
            counter
            outlined
            @click:append="show2 = !show2"
          ></v-text-field>
                    
                  </v-col>
                </v-row>
                
                <v-divider></v-divider>
                <v-row 
                    cols="12"
                    md="4"
                >
                  <v-col>
                    <v-btn
                      color="warning"
                     
                      @click="register"
                      depressed
                      block
                    >
                      Register
                    </v-btn>
                  </v-col>
                </v-row>
                <v-row 
                    cols="12"
                    md="4"
                >
                  <v-col>
                    <p class="text-center text--disabled">By signing up, you agree to sent easily's <a>Terms of service</a></p>
                  </v-col>
                </v-row>
              </v-container>
            </v-form>
             <v-form id="lform" ref="logform">
              <v-container>
                
                <v-row
                  cols="12"
                  md="4"
                >
                  <v-col>
                    <v-text-field
                      v-model="logusername"
                      :rules="[rules.required]"
                      label="username"
                      required
                      outlined
                      clearable
                    ></v-text-field>
                  </v-col>
                </v-row>
                
                <v-row
                    cols="12"
                    md="4"
                  >
                 
                  <v-col>
                   <v-text-field
            v-model="logpassword"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Normal with hint text"
            hint="At least 8 characters"
            counter
            outlined
            @click:append="show1 = !show1"
          ></v-text-field>
                    
                  </v-col>
                </v-row>
                
                
                <v-divider></v-divider>
                <v-row 
                    cols="12"
                    md="4"
                >
                  <v-col>
                    <v-btn
                      color="warning"
                      @click="login"
                      depressed
                      block
                    >
                      Login
                    </v-btn>
                  </v-col>
                </v-row>
                <v-row 
                    cols="12"
                    md="4"
                >
                  <v-col>
                    <p class="text-center text--disabled">By signing up, you agree to sent easily's <a>Terms of service</a></p>
                  </v-col>
                </v-row>
              </v-container>
            </v-form>
          </v-card>
        </v-col>
        <v-col class="hidden-xs-only" cols="1">
        </v-col>
      </v-row>

    </v-container>
    
   
  </div>
</template>

<script>
import axios from 'axios';
import router from "@/router/index.js";
import store from "@/store/index.js";

  export default {
    name: 'Login',
    data: () => {
      return {
        
        username: "",
        password: "",
        cpassword: "",
        show1: false,
        show2: false,
        regform: true,
        logform: true,
        logusername: "",
        logpassword: "",
        Email: "",
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          emailMatch: v => /.+@.+/.test(v) || 'E-mail must be valid',
          // passwordConfirmationRule: v =>(v===this.password)||'password does not match '
        }
        
      }
    },
    methods: {
      login () {
        if (this.$refs.logform.validate()) {
          
          var data = {
            username: this.logusername,
            password: this.logpassword
          }
          
          axios.defaults.baseURL = this.$store.state.baseURL;
          axios.defaults.headers.post['Content-Type'] = 'application/json';
            
          axios.post('/api/api-token-auth/',data)
          .then(function(response) {
                store.dispatch("executeUpdateToken",response["data"]["token"]);
                axios.defaults.headers.common['Authorization'] = 'Token '+response["data"]["token"];
                axios.get('/api/user/account/get_info/')
                .then(function(response) {
                      console.log(response)
                      store.dispatch("executeUpdateProfile",response["data"]);
                      router.replace({ name: 'dashboard' })
                })
                .catch(function(error) {
                    if (error.response) {
                      console.log(error.response)
                    }
                })
          })
          .catch(function(error) {
              if (error.response) {
                console.log(error.response)
              }
          })
        }
      },
      register () {
        if (this.$refs.regform.validate()) {
          
          var data = {
            email: this.Email,
            username: this.username,
            password: this.password
          }
          
          axios.defaults.baseURL = this.$store.state.baseURL;
          axios.defaults.headers.post['Content-Type'] = 'application/json';
            
          axios.post('/api/user/account/signup/',data)
          .then(function(response) {
            if(response.data=='success')
            {
               document.getElementById('lform').style.display='block';
               document.getElementById('rform').style.display='none';
               document.getElementById('rtctr').style.display='block';
               document.getElementById('ltctr').style.display='none';
            }       
              
          })
          .catch(function(error) {
              if (error.response) {
                console.log(error.response)
              }
          })
        }
      },
    },
    computed: {
    
    }
}
  
</script>

