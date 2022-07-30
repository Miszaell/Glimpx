<template>
  <div>
    <q-card flat bordered class="my-card bg-grey-1 text-black q-mb-md">
      <q-card-section>
        <div class="row items-center no-wrap">
          <div class="col">
            <div class="text-h6">{{ $t('heart.family') }}</div>
          </div>
        </div>
      </q-card-section>
      <q-card-section>
        <q-form class="q-gutter-md">
          <q-card-section horizontal>
            <q-card-section class="col-6">
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="family.neoplasm" label="Temperatura"
                dense />
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="family.chronic_degenerative_diseases"
                label="Pulso" dense />
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="family.metabolic_endocrine_diseases"
                label="Frecuencia cardiaca" dense />
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
  </div>
</template>

<script>
import { ref } from 'vue';
export default {
  name: "familyDetail",
  data() {
    return {
      family: ref([]),
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
        return this.compareObj(data.family_bkg, this.family)
      }
      return false
    },
    validateForm() {
      if (!this.family.neoplasm ||
        !this.family.chronic_degenerative_diseases ||
        !this.family.metabolic_endocrine_diseases) {
        Notify.create({
          type: "warning",
          position: "top-right",
          message: "Contesta todos los campos.",
        });
      } else {
        if (this.$route.name == 'manageAnamnesis') this.postFamily()
        else this.putFamily()
      }
    },
    getData() {
      let res = JSON.parse(sessionStorage.getItem("data"))
      this.row = res;
      this.family = res.family_bkg;
    },
    putFamily() {
      let data = JSON.parse(sessionStorage.getItem("data"))
      let formData = new FormData()
      formData.append("neoplasm", this.family.neoplasm)
      formData.append("chronic_degenerative_diseases", this.family.chronic_degenerative_diseases)
      formData.append("metabolic_endocrine_diseases", this.family.metabolic_endocrine_diseases)
      formData.append("user", this.family.user)
      if (!this.validateObjects('family')) {
        api.put(`familyBkg/${data.family_bkg.id}/`, formData)
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
    postFamily() {
      let patient = JSON.parse(sessionStorage.getItem("patient"))
      let formData = new FormData()
      formData.append("neoplasm", this.family.neoplasm)
      formData.append("chronic_degenerative_diseases", this.family.chronic_degenerative_diseases)
      formData.append("metabolic_endocrine_diseases", this.family.metabolic_endocrine_diseases)
      formData.append("user", patient.id)
      api.post(`familyBkg/`, formData)
        .then((res) => {
          if (res.status == 201) {
            this.edit = false
            this.$router.push({
              name: "consult"
            })
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
    editOff() {
      let data = JSON.parse(sessionStorage.getItem("data"))
      this.edit = false
      this.family = data.family_bkg;
    },
  },
}
</script>
