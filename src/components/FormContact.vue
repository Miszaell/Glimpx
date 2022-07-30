<template>
  <div>
    <q-card class="card shadow-9">
      <q-card-section>
        <q-form class="q-gutter-lg">
          <div>
            <q-input class="q-pt-md" type="text" v-model="email" :label="$t('contact.email')"
              :rules="[(val) => !!val || 'Campo obligatorio']">
              <template v-slot:append>
                <q-icon name="email" />
              </template>
            </q-input>
          </div>
          <div>
            <q-input v-model="text" filled clearable type="textarea" :label="$t('contact.message')">

            </q-input>
          </div>
          <div class="text-center">
            <q-btn rounded :label="$t('buttons.formContact')" icon="arrow_right_alt" color="positive" type="button"
              @click="loginRequest" />
          </div>
        </q-form>
      </q-card-section>
    </q-card>
  </div>
</template>
<script>

import api from 'src/api'
import { Notify } from 'quasar'

export default {
  setup() {

  },
  data() {
    return {
      email: "",
      text: "",
    }
  },
  methods: {
    loginRequest() {
      let formData = new FormData()
      formData.append("email", this.email)
      formData.append("text", this.text)
      api.post("comentarios/", formData).then((res) => {
        if (res.status == 201) {
          Notify.create({
            color: "primary",
            message: "Guardado"
          })
        }
      }).catch((error) => {
        Notify.create({
          color: "negative",
          message: "Error al guardar"
        })
      })
    }
  }
}
</script>
