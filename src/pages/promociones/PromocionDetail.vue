<template>
  <q-page padding>
    <q-toolbar inset>
      <q-breadcrumbs active-color="positive" style="font-size: 15px">
        <q-breadcrumbs-el icon="health_and_safety" to="promotions" label="Promociones de salud" />
        <q-breadcrumbs-el v-if="!row.title" icon="add" label="Crear" class="text-green" />
        <q-breadcrumbs-el :label="row.title" to="promotionDetail" class="text-green" />
      </q-breadcrumbs>
    </q-toolbar>
    <q-card flat bordered class="my-card bg-grey-1 text-black">
      <q-card-section>
        <div class="row items-center no-wrap">
          <div class="col">
            <div class="text-h6">{{ row.title }}</div>
          </div>
          <div class="col-auto">
            <q-btn color="grey-7" round flat icon="more_vert">
              <q-menu cover auto-close>
                <q-list>
                  <q-item clickable @click="deletePromo()">
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
              <q-input :readonly="!edit" class="q-ma-sm" filled v-model="row.title" label="Nombre" dense />
              <q-input :readonly="!edit" class="q-ma-sm" filled v-model="row.description" label="Descripción" dense />
            </q-card-section>
            <q-separator vertical />
            <q-card-section class="col-6">
              <q-input :readonly="!edit" class="q-ma-sm" filled v-model="row.startTime" label="Cantidad" dense />
              <q-input :readonly="!edit" class="q-ma-sm" filled v-model="row.endTime" label="UOM" dense />
            </q-card-section>
          </q-card-section>
          <q-separator />
          <q-card-section>
            <q-btn @click="validateForm()" :disable="validateObjects()" v-show="edit" class="q-mx-md"
              label="Guardar cambios" color="blue" icon="save" size="sm">
            </q-btn>
            <q-btn @click="editOff()" v-show="edit" class="q-mx-md" label="Descartar" color="red-9" icon="delete"
              size="sm">
            </q-btn>
            <q-btn @click="edit = true" v-show="!edit" class="q-mx-md" label="Editar" color="grey" icon="mode_edit"
              size="sm">
            </q-btn>
          </q-card-section>
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import { Notify } from "quasar";
import api from "src/api";
import { ref } from "vue";
export default {
  name: "PromotionDetail",
  data() {
    return {
      row: [],
      savepost: ref(true),
      saveput: ref(true),
      edit: ref(false),
    };
  },
  mounted() {
    if (sessionStorage.getItem("data")) {
      this.getData()
    }
    else {
      this.edit = true
    }
  },
  unmounted() {
    sessionStorage.removeItem("data")
  },
  methods: {
    compareObj(a, b) {
      var aKeys = Object.keys(a).sort();
      var bKeys = Object.keys(b).sort();
      if (aKeys.length !== bKeys.length) {
        return false;
      }
      if (aKeys.join('') !== bKeys.join('')) {
        return false;
      }
      for (var i = 0; i < aKeys.length; i++) {
        if (a[aKeys[i]] !== b[bKeys[i]]) {
          return false;
        }
      }
      return true;
    },
    validateObjects() {
      let data = JSON.parse(sessionStorage.getItem("data"))
      if (data) {
        return this.compareObj(data, this.row)
      }
      return false
    },
    validateForm() {
      if (!this.row.title ||
        !this.row.description ||
        !this.row.startTime ||
        !this.row.endTime) {
        Notify.create({
          type: "warning",
          position: "top-right",
          message: "Contesta todos los campos.",
        });
      } else {
        if (!sessionStorage.getItem("data")) this.postPromo()
        else this.putPromo()
      }
    },
    getData() {
      let res = JSON.parse(sessionStorage.getItem("data"))
      this.row = res;
    },
    putPromo() {
      let data = JSON.parse(sessionStorage.getItem("data"))
      let formData = new FormData()
      formData.append("title", this.row.title)
      formData.append("description", this.row.description)
      formData.append("startTime", this.row.startTime)
      formData.append("endTime", this.row.endTime)
      if (!this.validateObjects()) {
        api.put(`promotions/${data.id}/`, formData)
          .then((res) => {
            if (res.status == 200) {
              this.edit = false
              sessionStorage.setItem("data", JSON.stringify(this.row))
              Notify.create({
                type: "positive",
                position: "top-right",
                message: "Se ha actualizado el registro",
              });
            }
            else {
              Notify.create({
                type: "negative",
                position: "top-right",
                message: "Ocurrió un error inesperado, intenta otra vez.",
              });
            }
          })
          .catch((error) => {
            console.error(error.data.message)
            Notify.create({
              type: "negative",
              position: "top-right",
              message: "Ocurrió un error inesperado, intenta otra vez.",
            });
          })
      }
    },

    postPromo() {
      let formData = new FormData()
      formData.append("title", this.row.title)
      formData.append("description", this.row.description)
      formData.append("startTime", this.row.startTime)
      formData.append("endTime", this.row.endTime)
      if (!this.validateObjects()) {
        api.post(`promotions/`, formData)
          .then((res) => {
            if (res.status == 201) {
              this.edit = false
              Notify.create({
                type: "positive",
                position: "top-right",
                message: "Se ha guardado el registro",
              });
            }
            else {
              Notify.create({
                type: "negative",
                position: "top-right",
                message: "Ocurrió un error inesperado, intenta otra vez.",
              });
            }
          })
          .catch((error) => {
            console.error(error.data.message)
            Notify.create({
              type: "negative",
              position: "top-right",
              message: "Ocurrió un error inesperado, intenta otra vez.",
            });
          })
      }
    },

    deletePromo() {
      let data = JSON.parse(sessionStorage.getItem("data"))
      api.del(`promotions/${data.id}/`)
        .then((res) => {
          if (res.status == 200) {
            this.edit = false
            this.$router.push("stock")
            Notify.create({
              type: "positive",
              position: "top-right",
              message: "Se ha eliminado el registro",
            });
          }
          else {
            Notify.create({
              type: "negative",
              position: "top-right",
              message: "Ocurrió un error inesperado, intenta otra vez.",
            });
          }
        })
        .catch((error) => {
          console.error(error.data.message)
          Notify.create({
            type: "negative",
            position: "top-right",
            message: "Ocurrió un error inesperado, intenta otra vez.",
          });
        })
    },

    editOff() {
      let data = JSON.parse(sessionStorage.getItem("data"))
      this.edit = false
      this.row = data;
    },
  },
}
</script>
