<template>
  <q-page class="q-pa-sm">
    <div class="flex flex-center row q-col-gutter-sm">
      <div class="col-lg-8 col-md-8 col-xs-12 col-sm-12">
        <q-card>
          <q-card-section class="text-h6">
            <div v-if="!edit">
              <div class="text-h6">Editar perfil</div>
              <div class="text-subtitle2">Gestiona tu perfil</div>
            </div>
            <div v-if="edit">
              <div class="text-h6">Informción del perfil</div>
            </div>
          </q-card-section>
          <q-card-section class="q-pa-sm">
            <q-list class="row">
              <q-item class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <q-item-section side>
                  <div class="grid">
                    <figure class="effect">
                      <img v-if="user.avatar" :src="user.avatar" :alt="user.name" />
                      <figcaption>
                        <p>
                          <q-file borderless v-model="image" accept=".jpg, image/*" @change="onFilePicked">
                            <q-avatar icon="add_a_photo" color="secondary" text-color="white" />
                          </q-file>
                        </p>
                      </figcaption>
                    </figure>
                  </div>
                </q-item-section>
              </q-item>

              <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <q-item-section>
                  <q-input dense :readonly="edit" filled v-model="user.name" label="User Name" />
                </q-item-section>
              </q-item>
              <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <q-item-section>
                  <q-input dense :readonly="edit" filled v-model="user.email" label="Email Address" />
                </q-item-section>
              </q-item>
            </q-list>
          </q-card-section>
          <q-card-actions align="right">
            <q-btn @click="validateForm" v-show="!edit" label="Guardar cambios" color="blue" icon="save" size="sm">
            </q-btn>
            <q-btn @click="createOf" v-show="!edit" label="Descartar" color="red-9" icon="delete" size="sm"></q-btn>
            <q-btn @click="updateOn" v-show="edit" label="Editar" color="primary" icon="mode_edit" size="sm"></q-btn>
          </q-card-actions>
        </q-card>
      </div>
      <div class="col-lg-8 col-md-8 col-xs-12 col-sm-12">
        <q-card>
          <q-card-section class="text-h6 q-pa-sm">
            <div class="text-h6">Actualizar contraseña</div>
          </q-card-section>
          <q-card-section class="q-pa-sm row">
            <q-item class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
              <q-item-section> Contraseña actual </q-item-section>
            </q-item>
            <q-item class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
              <q-item-section>
                <q-input dense filled color="white" round v-model="user.currentPass" label="Contraseña actual" />
              </q-item-section>
            </q-item>
            <q-item class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
              <q-item-section> Nueva contraseña </q-item-section>
            </q-item>
            <q-item class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
              <q-item-section>
                <q-input dense filled color="white" round v-model="user.newPass" label="Nueva contraseña" />
              </q-item-section>
            </q-item>
            <q-item class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
              <q-item-section> Confirma la nueva contraseña </q-item-section>
            </q-item>
            <q-item class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
              <q-item-section>
                <q-input dense filled round color="white" v-model="user.confirmPass"
                  label="Confirma la nueva contraseña" />
              </q-item-section>
            </q-item>
          </q-card-section>
          <q-card-actions align="right">
            <q-btn @click="validatePass" label="Cambiar contraseña" color="blue" icon="save" size="sm"></q-btn>
          </q-card-actions>
        </q-card>
      </div>
    </div>
    <q-btn @click="setAdmin()" flat v-show="enb">ADM</q-btn>
  </q-page>
</template>

<script>
import { Notify } from "quasar";
import api from "src/api";
import { defineComponent } from "vue";
import { ref } from "vue";

export default defineComponent({
  name: "UserProfile",
  data() {
    return {
      enb: false,
      image: ref(null),
      imageFile: "",
      edit: true,
      editPassword: true,
      user: {
        name: "",
        email: "",
        currentPass: "",
        newPass: "",
        confirmPass: "",
        avatar: ref(null),
      },
      password_dict: {},
    };
  },
  created() {
    this.getUser();
  },
  methods: {
    setUser() {
      let usr = JSON.parse(sessionStorage.getItem("user"))
      api.get(`users/${usr.id}/`).then((res) => {
        let user = res.data
        this.user.name = user.name;
        this.user.email = user.email;
      });
    },
    getUser() {
      this.setUser();
      let user = JSON.parse(sessionStorage.getItem("user"));
      if (user) {
        this.user.avatar = 'http://localhost:8000' + user.image;
      }
    },


    createOf() {
      this.getUser();
      this.edit = true;
    },

    updateOn() {
      this.edit = false;
    },

    validateForm() {
      let rules = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
      if (!this.user.name || !this.user.email) {
        Notify.create({
          type: "warning",
          message: "Contesta todos los campos.",
        });
      } else {
        if (rules.exec(this.user.email)) {
          this.updateUser();
        } else {
          Notify.create({
            type: "warning",
            message: "Ingresa una direción de email valida.",
          });
        }
      }
    },

    validatePass() {
      if (
        !this.user.currentPass ||
        !this.user.newPass ||
        !this.user.confirmPass
      ) {
        Notify.create({
          type: "warning",
          message: "Contesta todos los campos.",
        });
      } else {
        if (this.user.newPass === this.user.confirmPass) {
          if (this.user.newPass.length >= 8) {
            this.updatePass();
          } else {
            Notify.create({
              type: "warning",
              message: "La nueva contraseña debe ser mayor a 8 caracteres.",
            });
          }
        } else {
          Notify.create({
            type: "warning",
            message: "Las contraseñas no coinciden.",
          });
        }
      }
    },

    updateUser() {
      let formData = new FormData();
      let userID = sessionStorage.getItem("userId");
      formData.append("id", userID);
      formData.append("name", this.user.name);
      formData.append("email", this.user.email);
      try {
        this.putProfile(formData);
        this.edit = true;
      } catch (error) {
        console.error(error);
      }
    },

    updatePass() {
      let formData = new FormData();
      let userID = sessionStorage.getItem("userId");
      formData.append("id", userID);
      formData.append("currentPassword", this.user.currentPass);
      formData.append("newPassword", this.user.newPass);
      try {
        this.updatePassword(formData);
      } catch (error) {
        console.error(error);
      }
    },

    onFilePicked(e) {
      const files = e.target.files;
      if (files[0] !== undefined) {
        this.image = files[0].name;
        var sizeByte = files[0].size;
        var siezekiloByte = parseInt(sizeByte / 1024);
        if (siezekiloByte > 2000) {
          Notify.create({
            type: "warning",
            message: "La imágen supera el tamaño establecido: 2mb",
          });
        } else {
          if (this.image.lastIndexOf(".") <= 0) {
            return;
          }
          const fr = new FileReader();
          fr.readAsDataURL(files[0]);
          fr.addEventListener("load", () => {
            this.imageFile = files[0];
            let userID = sessionStorage.getItem("userId");
            let formData = new FormData();
            formData.append("imagen", this.imageFile);
            formData.append("id", userID);
            try {
              this.postUsuarioImage(formData).then(() => {
                this.fetchusuarioId(userID).then(() => {
                  let urlsplit = localStorage
                    .getItem("auth_url")
                    .split("/api/")[0];
                  const res =
                    this.$store.getters["configuracion/getterUsuarioId"];
                  this.user.avatar = urlsplit + "/images/users/" + res[0].image;
                });
              });
            } catch (error) {
              console.error(error);
            }
          });
        }
      } else {
        this.image = "";
      }
    },

    setAdmin() {
      let formData = new FormData;
      formData.append("id", sessionStorage.getItem("userId"));
      formData.append("roleName", 'Admin');
      try {
        this.$store.dispatch("permisos/assignRole", formData);
      } catch (error) {
        console.error(error);
      }
    },
  },
});
</script>

<style scoped>
@import "../../css/profile.css";
</style>
