<template>
  <div>
    <q-card flat bordered class="my-card bg-grey-1 text-black q-mb-md">
      <q-card-section>
        <div class="row items-center no-wrap">
          <div class="col">
            <div class="text-h6">{{ $t('heart.clinic') }}</div>
          </div>
        </div>
      </q-card-section>
      <q-card-section>
        <q-form class="q-gutter-md">
          <q-card-section horizontal>
            <q-card-section class="col-6">
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="clinic.contagious_infections_desease"
                label="Enfermedades infecciosas/contagiosas" dense />
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="clinic.chronic_degenerative_disease"
                label="Enfermedades cronico degenerativas" dense />
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="clinic.traums" label="Traumas"
                dense />
            </q-card-section>
            <q-separator vertical />
            <q-card-section class="col-6">
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="clinic.allergic" label="Alergias"
                dense />
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="clinic.surgical" label="Cirugías"
                dense />
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="clinic.previous_hospitalizations"
                label="Hospitalizaciones previas" dense />
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="clinic.transfusions"
                label="Transfusiones" dense />
              <q-input autogrow :readonly="!edit" class="q-ma-sm" filled v-model="clinic.drugs_addiction_alcoholism"
                label="Alcoholismo o adicciones" dense />
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
import { ref } from 'vue'
import { Notify } from 'quasar';
import api from 'src/api';
export default {
  name: "ClinicDetail",
  data() {
    return {
      clinic: ref({}),
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
        return this.compareObj(data.clinical_exp, this.clinic)
      }
      return false
    },
    validateForm() {
      if (!this.clinic.contagious_infections_desease ||
        !this.clinic.chronic_degenerative_disease ||
        !this.clinic.traums ||
        !this.clinic.allergic ||
        !this.clinic.surgical ||
        !this.clinic.previous_hospitalizations ||
        !this.clinic.transfusions ||
        !this.clinic.drugs_addiction_alcoholism) {
        Notify.create({
          type: "warning",
          position: "top-right",
          message: "Contesta todos los campos.",
        });
      } else {
        if (this.$route.name == 'manageAnamnesis') this.postClinical()
        else this.putClinical()
      }
    },
    getData() {
      let res = JSON.parse(sessionStorage.getItem("data"))
      this.row = res;
      this.clinic = res.clinical_exp;
    },
    putClinical() {
      let data = JSON.parse(sessionStorage.getItem("data"))
      let formData = new FormData()
      formData.append("contagious_infections_desease", this.clinic.contagious_infections_desease)
      formData.append("chronic_degenerative_disease", this.clinic.chronic_degenerative_disease)
      formData.append("traums", this.clinic.traums)
      formData.append("allergic", this.clinic.allergic)
      formData.append("surgical", this.clinic.surgical)
      formData.append("previous_hospitalizations", this.clinic.previous_hospitalizations)
      formData.append("transfusions", this.clinic.transfusions)
      formData.append("drugs_addiction_alcoholism", this.clinic.drugs_addiction_alcoholism)
      formData.append("user", this.clinic.user)
      if (!this.validateObjects('clinic')) {
        api.put(`clinicalExm/${data.clinical_exp.id}/`, formData)
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
    postClinical() {
      let patient = JSON.parse(sessionStorage.getItem("patient"))
      let formData = new FormData()
      formData.append("contagious_infections_desease", this.clinic.contagious_infections_desease)
      formData.append("chronic_degenerative_disease", this.clinic.chronic_degenerative_disease)
      formData.append("traums", this.clinic.traums)
      formData.append("allergic", this.clinic.allergic)
      formData.append("surgical", this.clinic.surgical)
      formData.append("previous_hospitalizations", this.clinic.previous_hospitalizations)
      formData.append("transfusions", this.clinic.transfusions)
      formData.append("drugs_addiction_alcoholism", this.clinic.drugs_addiction_alcoholism)
      formData.append("user", patient.id)
      api.post(`clinicalExm/`, formData)
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
      this.clinic = data.clinical_exp;
    },
  },
}
</script>
