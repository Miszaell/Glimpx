<template>
  <div>
    <q-card class="my-card" flat bordered>
      <q-card-section horizontal>
        <q-card-section class="col">
          <div class="text-h6">{{ $t('contact.phone') }}</div>
          <div>55-37-21-53-43</div>
          <div>56-13-75-34-27</div>
        </q-card-section>

        <q-separator vertical />

        <q-card-section class="col">
          <div class="text-h6">{{ $t('contact.email') }}</div>
          <div>alvarezkareng@gmail.com</div>
          <div>villegasmisaelg@gmail.com</div>
        </q-card-section>

        <q-separator vertical />

        <q-card-section class="col">
          <div class="text-h6">CEO</div>
          <div>Ana Karen Alvarez Garcia</div>
          <div class="text-h6">CTO</div>
          <div> Misael Villegas Gonzales</div>
        </q-card-section>
      </q-card-section>
    </q-card>
  </div>
</template>
<script>
export default {
  setup() {

  },
}
</script>
