<template>
  <q-page padding class="text-justify" style="padding-left: 8%; padding-right: 8%;">
    <div class="flex flex-center">
      <q-img src="icons/favicon-128x128.png" width="80px"></q-img>
    </div>
    <div class="flex flex-center text-justify">
      {{ $t('aviso.p1') }}
    </div>

    <div class="text-bold q-my-md">{{ $t('aviso.s1') }}</div>

    <div class="q-my-md flex text-justify">

      <div class="q-my-md">

        {{ $t('aviso.p2') }}
      </div>
      {{ $t('aviso.p3') }}

    </div>

    ​<div class="q-my-md flex text-justify">
      {{ $t('aviso.p4') }}
    </div>
    <div class="text-bold q-my-md">{{ $t('aviso.s2') }} </div>

    ​<div class="q-my-md flex text-justify">
      {{ $t('aviso.s3') }}
      <ul>
        <li>{{ $t('aviso.l1') }}</li>
        <li>{{ $t('aviso.l2') }} </li>
        <li>{{ $t('aviso.l3') }}</li>
        <li>{{ $t('aviso.l4') }}</li>
      </ul>

      ​
    </div>

    <div class="text-bold q-my-md">{{ $t('aviso.s4') }}</div>
    ​<div class="q-my-md flex text-justify">

      {{ $t('aviso.s5') }}<br>

      {{ $t('aviso.s6') }}
      <ul>
        <li> {{ $t('aviso.l5') }}</li>
        <li> {{ $t('aviso.l6') }}</li>
        <li> {{ $t('aviso.l7') }}</li>
        <li> {{ $t('aviso.l8') }}</li>
        <li> {{ $t('aviso.l9') }}</li>
        <li> {{ $t('aviso.l10') }}</li>
        <li> {{ $t('aviso.l11') }}</li>
        <li> {{ $t('aviso.l12') }}</li>
        <li> {{ $t('aviso.l13') }}</li>
        <li> {{ $t('aviso.l14') }}</li>
        <li> {{ $t('aviso.l15') }}</li>
        <li> {{ $t('aviso.l16') }}</li>
      </ul>
    </div>
    ​
    ​<div class="q-my-md flex text-justify">
      {{ $t('aviso.p9') }}
      <ul>
        <li>{{ $t('aviso.l17') }}</li>
        <li>{{ $t('aviso.l18') }}</li>
        <li>{{ $t('aviso.l19') }}</li>
        <li>{{ $t('aviso.l20') }}</li>
        <li>{{ $t('aviso.l21') }}</li>
        <li>{{ $t('aviso.l22') }}</li>
        <li>{{ $t('aviso.l23') }}</li>
        <li>{{ $t('aviso.l24') }}</li>
      </ul>
      ​ ​
    </div>

    <div class="q-my-md flex text-justify">
      <div class="text-bold q-my-md">{{ $t('aviso.s7') }}</div>
      {{ $t('aviso.p5') }}
    </div>

    <div class="q-my-md flex text-justify">
      <div class="text-bold q-my-md">{{ $t('aviso.s8') }}</div>

      <ul>
        <li>{{ $t('aviso.l25') }}</li>
        <li>{{ $t('aviso.l26') }}</li>
        <li>{{ $t('aviso.l27') }}</li>
        <li>{{ $t('aviso.l28') }}</li>
        <li>{{ $t('aviso.l29') }}</li>
      </ul>
      {{ $t('aviso.p6') }}
    </div>

    <div class="q-my-md flex text-justify">
      <div class="text-bold q-my-md">{{ $t('aviso.s9') }}</div>
      {{ $t('aviso.p7') }}

    </div>

    <div class="q-my-md flex text-justify">
      <div class="text-bold q-my-md">{{ $t('aviso.s10') }}</div>
      {{ $t('aviso.p8') }}

    </div>
  </q-page>
</template>

<script>
export default {
  name: "AvisoPage"
}
</script>
