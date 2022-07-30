<template>
  <q-page padding>
    <div>
      <q-toolbar inset>
        <q-breadcrumbs active-color="positive" style="font-size: 15px">
          <q-breadcrumbs-el icon="inventory_2" to="users" label="Usuario" />
          <q-breadcrumbs-el v-if="!row.name" icon="add" label="Crear" />
          <q-breadcrumbs-el :label="row.name" to="user-detail" class="text-green" />
        </q-breadcrumbs>
      </q-toolbar>
      <q-card flat bordered class="my-card bg-grey-1 text-black">
        <q-card-section>
          <div class="row items-center no-wrap">
            <div class="col">
              <div class="text-h6">{{ row.name }}</div>
            </div>
            <!-- <div class="col-3">
              <q-btn-toggle v-model="row.state" spread :readonly="edit" size="sm" class="my-custom-toggle" no-caps
                rounded toggle-color="blue-grey-5" color="white" text-color="visuel" :options="[
                  { label: 'Activo', value: 'open' },
                  { label: 'Inactivo', value: 'close' },
                ]" />
            </div> -->
            <div class="col-auto">
              <q-btn color="grey-7" round flat icon="more_vert">
                <q-menu cover auto-close>
                  <q-list>
                    <q-item clickable @click="deleteUser">
                      <q-item-section>Eliminar</q-item-section>
                    </q-item>
                  </q-list>
                </q-menu>
              </q-btn>
            </div>
          </div>
        </q-card-section>
        <q-card-section>
          <q-form class="q-gutter-md">
            <q-card-section horizontal>
              <q-card-section class="col-6">
                <q-input :readonly="edit" filled v-model="row.name" label="Nombre *" lazy-rules dense :rules="[
                  (val) => (val && val.length > 0) || 'Please type something',
                ]" />
                <q-input :readonly="edit" filled v-model="row.email" label="Correo *" dense lazy-rules :rules="[
                  (val) => (val && val.length > 0) || 'Please type something',
                ]" />
                <q-input :readonly="edit" filled v-model="password" label="Contraseña *" dense lazy-rules :rules="[
                  (val) => (val && val.length > 0) || 'Please type something',
                ]" />
              </q-card-section>
              <q-separator vertical />
              <q-card-section class="col-6">
                <q-input :readonly="edit" filled v-model="row.username" label="Username *" dense lazy-rules :rules="[
                  (val) => (val && val.length > 0) || 'Please type something',
                ]" />
                <q-input :readonly="edit" filled v-model="row.last_name" label="Last name *" dense lazy-rules :rules="[
                  (val) => (val && val.length > 0) || 'Please type something',
                ]" />
                <q-btn class="q-ma-md" @click="randomPass" v-show="!savepost" label="Generar contraseña" color="green"
                  icon="key" size="sm"></q-btn>
              </q-card-section>
            </q-card-section>
          </q-form>
        </q-card-section>

        <q-separator />
        <q-card-section>
          <div class="row items-center no-wrap">
            <div class="col">
              <div class="q-pa-md q-gutter-sm text-h6">
                <q-btn @click="validateForm('put')" v-show="!saveput" label="Guardar cambios" color="blue" icon="save"
                  size="sm">
                </q-btn>
                <q-btn @click="validateForm('created')" v-show="!savepost" label="Guardar" color="blue" icon="save"
                  size="sm">
                </q-btn>
                <q-btn @click="createOf" v-show="!edit" label="Descartar" color="red-9" icon="delete" size="sm">
                </q-btn>
                <q-btn @click="updateOn" v-show="edit" label="Editar" color="grey" icon="mode_edit" size="sm">
                </q-btn>
              </div>
            </div>
            <div class="col">
              <div class="q-pa-md q-gutter-sm text-h6" align="right">
                <q-btn size="sm" v-show="!edit" @click="resetPass()" label="Generar nueva contraseña" color="blue-9"
                  icon="key" />
                <q-btn @click="dialogImage = true" v-show="row.image" label="Ver foto" color="secondary" icon="camera"
                  size="sm">
                </q-btn>
                <q-btn size="sm" v-show="edit" @click="createOn" label="Crear" color="secondary" icon="add">
                </q-btn>
              </div>
            </div>
          </div>
        </q-card-section>
        <q-separator />
      </q-card>
    </div>
    <br />
    <q-dialog v-model="dialogImage">
      <q-layout view="hHh Lpr fFf" container class="bg-white" style="max-width: 400px; max-height: 550px;">
        <q-page-container>
          <q-page padding>
            <q-img :src="`http://localhost:8000${row.image}`" width="350px" height="500px">
              <div class="absolute-bottom text-subtitle1 text-center">
                {{ row.image.split('/media/perfil/')[1] }}
              </div>
            </q-img>
          </q-page>
        </q-page-container>
      </q-layout>
    </q-dialog>
    <q-dialog v-model="dialogPass" persistent>
      <q-layout view="hHh Lpr fFf" container class="bg-white" style="max-height: 350px">
        <q-header class="bg-visuel">
          <q-toolbar>
            <q-toolbar-title>Nueva contraseña</q-toolbar-title>
            <q-btn flat v-close-popup round dense icon="close" />
          </q-toolbar>
        </q-header>
        <q-page-container>
          <q-page padding>
            <p>
              <q-list bordered class="rounded-borders" style="min-width: 300px; min-height: 100px">
                <q-item>
                  <q-item-section class="q-pa-lg">
                    <p class="text-center q-mb-xl" style="font-size: large">
                      Se ha actualizado la contraseña
                    </p>
                    <p class="text-center" style="font-size: xx-large">
                      {{ password }}
                    </p>
                  </q-item-section>
                </q-item>
              </q-list>
            </p>
          </q-page>
        </q-page-container>
        <q-footer class="bg-visuel text-white">
          <q-toolbar inset> </q-toolbar>
        </q-footer>
      </q-layout>
    </q-dialog>
  </q-page>
</template>

<script>
import { Notify } from "quasar";
import api from "src/api";
import { ref } from "vue";
export default {
  name: "usuarios_detalle",
  data() {
    return {
      dialogPass: false,
      dialogImage: false,
      row: [],
      rows: [],
      rowspre: [],
      password: "",
      randomPassword: "",
      isPwd: ref(true),
      savepost: true,
      saveput: true,
      edit: true,
      roles: [],
      role: "",
    };
  },


  mounted() {
    this.fetchUsuarioId();
  },
  created() { },

  methods: {

    dismiss() {
      this.rows.name = "";
      this.rows.email = "";
      this.rows.username = "";
      this.rows.last_name = "";
      this.rows.tipo = "";
      this.rows.state = "";
      this.password = null;
      this.confirm = false;
      this.edit = true;
      this.savepost = true;
      this.saveput = true;
      this.$router.push({
        path: "usuarios",
      });
    },
    randomPass() {
      for (let i = 0; i < 10; i++) {
        this.randomPassword += String.fromCharCode(
          (Math.floor(Math.random() * 100) % 94) + 33
        );
      }
      this.password = this.randomPassword;
      this.randomPassword = "";
    },
    validate() {
      if (this.user) {
        this.rows = JSON.parse(this.user);
      } else {
        this.rows.name = "";
        this.rows.email = null;
        this.rows.tipo = "";
        this.rows.state = "";
        this.password = null;
        this.edit = false;
        this.savepost = false;
      }
    },
    validateForm(form) {
      let rules = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
      if (form == "created") {
        if (
          !this.row.name ||
          !this.row.email ||
          !this.row.username ||
          !this.row.last_name ||
          !this.password
        ) {
          Notify.create({
            type: "warning",
            message: "Contesta todos los campos.",
          });
        } else {
          if (rules.exec(this.row.email)) {
            this.saveNew();
          } else {
            Notify.create({
              type: "warning",
              message: "Ingresa una direción de email valida.",
            });
          }
        }
      } else {
        if (!this.row.name || !this.row.email || !this.row.username || !this.row.last_name) {
          Notify.create({
            type: "warning",
            message: "Contesta todos los campos.",
          });
        } else {
          if (rules.exec(this.row.email)) {
            this.save();
          } else {
            Notify.create({
              type: "warning",
              message: "Ingresa una direción de email valida.",
            });
          }
        }
      }
    },
    fetchUsuarioId() {
      if (this.$route.params.action == "new") {
        this.createOn();
      } else {
        api
          .get(`users/${this.$route.params.id}/`)
          .then((res) => {
            this.row = res.data;
            this.rows = res.data;
          });
      }
    },
    saveNew() {
      let formData = new FormData();
      formData.append("name", this.row.name);
      formData.append("username", this.row.username);
      formData.append("last_name", this.row.last_name);
      formData.append("email", this.row.email);
      formData.append("password", this.password);
      api.post(`users/`, formData)
        .then((response) => {
          if (response.status == 201) {
            this.$router.push({
              name: "users",
            });
          }
        })
        .catch((error) => {
          Notify.create({
            type: "negative",
            message: "Ocurrió un error al guardar el elemento ",
          });
          console.log(error);
        });
    },
    save() {
      let formData = new FormData();
      formData.append("name", this.row.name);
      formData.append("username", this.row.username);
      formData.append("email", this.row.email);
      formData.append("image", this.row.image);

      api.put(`users/${this.$route.params.id}/`, formData)
        .then((response) => {
          this.edit = true;
          this.saveput = true;
          if (response.status == 200) {
            Notify.create({
              type: "positive",
              message: "Registro actualizado",
            });
          }
        })
        .catch((error) => {
          Notify.create({
            type: "negative",
            message: "Ocurrió un error al actualizar el elemento ",
          });
          console.error(error);
        });
    },
    deleteUser() {
      api.del(`users/${this.$route.params.id}/`)
        .then((res) => {
          this.$router.push({
            path: "/users",
          });
        })
        .catch((error) => {
          Notify.create({
            type: "negative",
            message: "Error al modificar",
          });
          console.error(error);
        });
    },
    createOn() {
      this.savepost = false;
      this.rowspre = this.rows;
      this.row = {
        id: "",
        name: "",
        email: "",
        tipo: "",
        state: "open",
      };
      this.edit = false;
      this.saveput = true;
    },
    createOf() {
      if (this.$route.params.action == "new") {
        this.$router.push({
          path: "/usuarios",
        });
      } else {
        if (this.rowspre) {
          this.row = this.rowspre;
        } else if (this.rowspre) {
          this.rowspre = this.row;
        }
        this.edit = true;
        this.savepost = true;
        this.saveput = true;
      }
    },
    updateOn() {
      this.rowspre = this.row;
      this.edit = false;
      this.saveput = false;
    },
    resetPass() {
      this.randomPass();
      let formData = new FormData();
      formData.append("id", this.row.id);
      formData.append("newPassword", this.password);
      console.log(this.password);
      try {
        this.dialogPass = true;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
