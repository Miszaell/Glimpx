<template>
  <div>
    <q-card flat bordered class="my-card bg-grey-1 text-black q-mb-md">
      <q-card-section>
        <div class="row items-center no-wrap">
          <div class="col">
            <div class="text-h6">{{ $t('heart.physic') }}</div>
          </div>
        </div>
      </q-card-section>
      <q-card-section>
        <q-form class="q-gutter-md">
          <q-card-section horizontal>
            <q-card-section class="col-6">
              <q-input :readonly="!edit" type="number" class="q-ma-sm" filled v-model="physic.temperature"
                label="Temperatura" dense />
              <q-input :readonly="!edit" type="number" class="q-ma-sm" filled v-model="physic.pulse" label="Pulso"
                dense />
              <q-input :readonly="!edit" type="number" class="q-ma-sm" filled v-model="physic.heart_rate"
                label="Frecuencia cardiaca" dense />
            </q-card-section>
            <q-separator vertical />
            <q-card-section class="col-6">
              <q-input :readonly="!edit" type="number" class="q-ma-sm" filled v-model="physic.breathing_rate"
                label="Frecuencia respiratoria" dense />
              <q-input :readonly="!edit" type="number" class="q-ma-sm" filled v-model="physic.weight" label="Talla"
                dense />
              <q-input :readonly="!edit" type="number" class="q-ma-sm" filled v-model="physic.height" label="Altura"
                dense />
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
            <q-btn @click="editOn()" v-show="!edit" class="q-mx-md" label="Editar" color="grey" icon="mode_edit"
              size="sm">
            </q-btn>
          </q-card-section>
        </q-form>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { ref } from 'vue'
import { Notify } from 'quasar'
import api from 'src/api'
export default {
  name: "physicDetail",
  props: {
    postReq: Boolean
  },
  watch: {
    postReq: function () {
      if (this.postReq == true) this.validateForm()
    }
  },
  data() {
    return {
      physic: ref([]),
      row: ref({}),
      edit: ref(false),
    }
  },
  created() {
    if (sessionStorage.getItem("data")) {
      this.getData();
    }
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
        return this.compareObj(data.physical_exp, this.physic)
      }
      return false
    },
    validateForm() {
      if (!this.physic.temperature ||
        !this.physic.pulse ||
        !this.physic.heart_rate ||
        !this.physic.breathing_rate ||
        !this.physic.weight ||
        !this.physic.height) {
        Notify.create({
          type: "warning",
          position: "top-right",
          message: "Contesta todos los campos.",
        });
      } else {
        if (this.$route.name == 'manageAnamnesis') this.postPhysic()
        else this.putPhysic()
      }
    },
    getData() {
      let res = JSON.parse(sessionStorage.getItem("data"))
      this.row = res;
      this.physic = res.physical_exp;
    },
    putPhysic() {
      let data = JSON.parse(sessionStorage.getItem("data"))
      let formData = new FormData()
      formData.append("temperature", this.physic.temperature)
      formData.append("pulse", this.physic.pulse)
      formData.append("heart_rate", this.physic.heart_rate)
      formData.append("breathing_rate", this.physic.breathing_rate)
      formData.append("weight", this.physic.weight)
      formData.append("height", this.physic.height)
      formData.append("user", this.physic.user)
      if (!this.validateObjects('physic')) {
        api.put(`physicalExm/${data.physical_exp.id}/`, formData)
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

    postPhysic() {
      let patient = JSON.parse(sessionStorage.getItem("patient"))
      let formData = new FormData()
      formData.append("temperature", this.physic.temperature)
      formData.append("pulse", this.physic.pulse)
      formData.append("heart_rate", this.physic.heart_rate)
      formData.append("breathing_rate", this.physic.breathing_rate)
      formData.append("weight", this.physic.weight)
      formData.append("height", this.physic.height)
      formData.append("user", patient.id)
      api.post('physicalExm/', formData).then((res) => {
        if (res.status == 201) {
          this.edit = false
          this.$emit("update:step", 3)
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
    },
    editOn() {
      this.edit = true
    },
    editOff() {
      let data = JSON.parse(sessionStorage.getItem("data"))
      this.edit = false
      this.physic = data.physical_exp;
    },
  }
}
</script>
