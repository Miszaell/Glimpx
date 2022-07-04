<template>
  <div>
    <q-card class="card shadow-9">
      <q-card-section>
        <q-form class="q-gutter-lg">
          <div class="flex flex-center">
            <q-input class="q-pt-md" type="text" v-model="login.username" label="Username"
              :rules="[(val) => !!val || 'Campo obligatorio']">
              <template v-slot:append>
                <q-icon name="person" />
              </template>
            </q-input>
          </div>
          <div class="flex flex-center">
            <q-input class="q-pt-md" type="email" v-model="login.email" label="Email"
              :rules="[(val) => !!val || 'Campo obligatorio']">
              <template v-slot:append>
                <q-icon name="email" />
              </template>
            </q-input>
          </div>
          <div class="flex flex-center">
            <q-input v-on:keyup.enter="loginRequest" class="q-pt-md" :type="isPwd ? 'password' : 'text'"
              v-model="login.password" label="Password" :rules="[(val) => !!val || 'Campo obligatorio']">
              <template v-slot:append>
                <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer"
                  @click="isPwd = !isPwd" />
              </template>
            </q-input>
          </div>
          <div class="text-center">
            <q-btn rounded :label="$t('buttons.btnAuth')" icon="arrow_right_alt" color="positive" type="button"
              @click="RegisterRequest" />
          </div>
        </q-form>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { Notify } from "quasar";
import { ref } from "vue";
export default {
  name: "loginPage",
  setup() {
    return {
      isPwd: ref(true),
      rememberMe: ref(false),
    };
  },
  data() {
    return {
      login: {
        email: null,
        password: null,
        username: null,
      },
      empresa: [],
      logoIMG: "",
      permissions: [],
      isAdmin: false,
    };
  },
  methods: {
    RegisterRequest() {
      if (
        this.login.email != null ||
        this.login.password != null ||
        this.login.email != "" ||
        this.login.password != ""
      ) {
        let formData = new FormData
        formData.append("password", this.login.password)
        formData.append("email", this.login.email)
        formData.append("username", this.login.username)
        this.$api.post("users/", formData)
          .then((response) => {

          })
          .catch((error) => {
            console.log(error);
          });
        Notify.create({
          type: "success",
          message: "Login",
        });
      } else {
        Notify.create({
          type: "warning",
          message: "Hay campos vacios",
        });
      }
    },
  },
};
</script>
