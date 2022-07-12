<template>
  <div>
    <q-card class="card shadow-9">
      <q-card-section>
        <q-form class="q-gutter-lg">
          <div>
            <q-input class="q-pt-md" type="text" v-model="email" label="Email"
              :rules="[(val) => !!val || 'Campo obligatorio']">
              <template v-slot:append>
                <q-icon name="email" />
              </template>
            </q-input>
          </div>
          <div>
            <q-input v-model="text" filled clearable type="textarea" label="mensaje">

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
export default {
  setup() {

  },
  data() {
    return {
      email: "",
      text: "",
    }
  }
}
</script>
