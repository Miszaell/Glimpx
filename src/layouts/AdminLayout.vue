<template>
  <q-layout view="lHh Lpr fff" class="bg-grey-1">
    <q-header elevated class="bg-white text-grey-8" height-hint="64">
      <q-toolbar class="GPL__toolbar" style="height: 64px">
        <q-btn flat dense round @click="toggleLeftDrawer" aria-label="Menu" icon="menu" class="q-mx-md" />

        <q-toolbar-title v-if="$q.screen.gt.sm" shrink class="row items-center no-wrap">
          <span class="q-ml-sm">{{ $t("main.appTitle") }}</span>
        </q-toolbar-title>

        <q-space />

        <q-select ref="search" dense borderless color="white" use-input class="GL__toolbar-select text-black"
          label="Search or jump to..." v-model="text" :options="filteredOptions" @filter="filter" style="width: 400px">
          <template v-slot:no-option>
            <q-item class="bg-white">
              <q-item-section>
                <div class="text-center">
                  <q-spinner-pie color="grey-5" size="24px" />
                </div>
              </q-item-section>
            </q-item>
          </template>

          <template v-slot:option="scope">
            <q-item v-bind="scope.itemProps" class="GL__select-GL__menu-link bg-white">
              <q-item-section side>
                <q-icon name="collections_bookmark" color="black" />
              </q-item-section>
              <q-item-section>
                <q-item-label v-html="$t(`dashboard.menu.${scope.opt.label}`)" class="text-black" />
              </q-item-section>
              <q-item-section side :class="{ 'default-type': !scope.opt.type }">
                <q-btn outline dense no-caps text-color="blue-grey-5" size="12px" class="bg-grey-1 q-px-sm">
                  {{ scope.opt.type || "Jump to" }}
                  <q-icon name="subdirectory_arrow_left" size="14px" />
                </q-btn>
              </q-item-section>
            </q-item>
          </template>
        </q-select>

        <q-btn v-if="$q.screen.gt.xs" flat dense no-wrap color="primary" icon="add" no-caps label="Create"
          class="q-ml-sm q-px-md">
          <q-menu anchor="top end" self="top end">
            <q-list class="text-grey-8" style="min-width: 100px">
              <q-item aria-hidden="true">
                <q-item-section class="text-uppercase text-grey-7" style="font-size: 0.7rem">Create New</q-item-section>
              </q-item>
              <q-item v-for="menu in createMenu" :key="menu.text" clickable v-close-popup aria-hidden="true">
                <q-item-section avatar>
                  <q-icon :name="menu.icon" />
                </q-item-section>
                <q-item-section>{{ menu.text }}</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-btn>

        <q-btn v-if="$q.screen.gt.xs" flat dense no-wrap color="primary" icon="cloud_upload" no-caps label="Upload"
          class="q-ml-sm q-px-md" />

        <q-space />

        <div class="q-gutter-sm row items-center no-wrap">
          <q-btn round dense flat color="text-grey-7" icon="translate">
            <q-menu :offset="[50, 10]">
              <q-list style="min-width: 50px">
                <q-item clickable v-close-popup @click="setLanguage('es-MX')">
                  <q-item-section>ES MX</q-item-section>
                </q-item>
                <q-item clickable v-close-popup @click="setLanguage('en-US')">
                  <q-item-section>EN US</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
          <q-btn round dense flat color=" grey-8" icon="notifications">
            <q-badge color="red" text-color="white" floating> 2 </q-badge>
            <q-tooltip>Notifications</q-tooltip>
          </q-btn>
          <q-btn round flat>
            <q-avatar size="26px">
              <img :src="image" />
            </q-avatar>
            <q-menu>
              <q-list style="min-width: 100px">
                <q-item clickable v-close-popup to="perfil">
                  <q-item-section>{{ username }}</q-item-section>
                </q-item>
                <q-item clickable v-close-popup to="/">
                  <q-item-section>Ir a hompage</q-item-section>
                </q-item>
                <q-item clickable v-close-popup @click="logoutRequest">
                  <q-item-section>{{ $t('main.logout') }}</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" bordered behavior="mobile" @click="leftDrawerOpen = false">
      <q-scroll-area class="fit">
        <q-toolbar class="GPL__toolbar">
          <q-toolbar-title class="row items-center text-grey-8">
            <span class="q-ml-sm">{{ $t("main.appTitle") }}</span>
          </q-toolbar-title>
        </q-toolbar>

        <q-list padding>
          <q-item v-for="link in links1" :key="link.text" clickable class="GPL__drawer-item" :to="link.url">
            <q-item-section avatar>
              <q-icon :name="link.icon" />
            </q-item-section>
            <q-item-section>
              <q-item-label>{{
                  $t(`dashboard.menu.${link.text}`)
              }}</q-item-label>
            </q-item-section>
          </q-item>

          <q-separator class="q-my-md" />

          <q-item v-for="link in links2" :key="link.text" clickable class="GPL__drawer-item">
            <q-item-section avatar>
              <q-icon :name="link.icon" />
            </q-item-section>
            <q-item-section>
              <q-item-label>{{
                  $t(`dashboard.menu.${link.text}`)
              }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from "vue";
import { Notify } from "quasar";
const stringOptions = ["hlPromotions"];

export default {
  name: "GooglePhotosLayout",

  setup() {
    const filteredOptions = ref([]);
    const leftDrawerOpen = ref(false);
    const search = ref(null);
    const storage = ref(0.26);
    const options = ref(null);
    const text = ref("");

    function filter(val, update) {
      if (options.value === null) {
        // load data
        setTimeout(() => {
          options.value = stringOptions;
          search.value.filter("");
        }, 1000);
        update();
        return;
      }
      if (val === "") {
        update(() => {
          filteredOptions.value = options.value.map((op) => ({ label: op }));
        });
        return;
      }
      update(() => {
        filteredOptions.value = [
          {
            label: val,
            type: "In this repository",
          },
          {
            label: val,
            type: "All GitHub",
          },
          ...options.value
            .filter((op) => op.toLowerCase().includes(val.toLowerCase()))
            .map((op) => ({ label: op })),
        ];
      });
    }
    function toggleLeftDrawer() {
      leftDrawerOpen.value = !leftDrawerOpen.value;
    }

    return {
      leftDrawerOpen,
      text,
      filteredOptions,
      search,
      filter,
      storage,
      toggleLeftDrawer,

      links1: [
        { icon: "people", text: "users", url: "users" },
        { icon: "inventory", text: "stock", url: "stock" },
        { icon: "health_and_safety", text: "hlPromotions", url: "usehlPromotionsrs" },
        { icon: "medication", text: "consult", url: "consult" },
      ],
      links2: [
        { icon: "settings", text: "settings" },
        { icon: "security", text: "roles" },
      ],
      createMenu: [
        { icon: "photo_album", text: "Album" },
        { icon: "people", text: "Shared Album" },
        { icon: "movie", text: "Movie" },
        { icon: "library_books", text: "Animation" },
        { icon: "dashboard", text: "Collage" },
        { icon: "book", text: "Photo book" },
      ],
    };
  },

  data() {
    return {
      username: null,
      image: "https://cdn.quasar.dev/img/boy-avatar.png"
    }
  },
  created() {
    let user = JSON.parse(sessionStorage.getItem("user"))
    if (user) {
      this.image = `http://localhost:8000${user.image}`
      this.username = user.email
    }
  },
  methods: {
    setLanguage(locale) {
      this.$root.$i18n.locale = locale;
    },
    currentLanguage() {
      return this.$i18n.locale === "es-MX" ? "en-US" : this.$i18n.locale;
    },

    logoutRequest() {
      let formData = new FormData
      formData.append("token", sessionStorage.getItem("token"))
      this.$api.post("logout/", formData)
        .then((response) => {
          if (response.status === 200) {
            sessionStorage.clear()
            this.$router.push("auth")
          }
        })
        .catch((error) => {
          Notify.create({
            type: "negative",
            message: this.$t('main.logoutError'),
          });
          console.error(error);
        });
    },
  },
};
</script>

<style lang="sass">
.GPL

  &__toolbar
    height: 64px

  &__toolbar-input
    width: 35%

  &__drawer-item
    line-height: 24px
    border-radius: 0 24px 24px 0
    margin-right: 12px

    .q-item__section--avatar
      padding-left: 12px
      .q-icon
        color: #5f6368

    .q-item__label:not(.q-item__label--caption)
      color: #3c4043
      letter-spacing: .01785714em
      font-size: .875rem
      font-weight: 500
      line-height: 1.25rem

    &--storage
      border-radius: 0
      margin-right: 0
      padding-top: 24px
      padding-bottom: 24px

  &__side-btn
    &__label
      font-size: 12px
      line-height: 24px
      letter-spacing: .01785714em
      font-weight: 500

  @media (min-width: 1024px)
    &__page-container
      padding-left: 94px
</style>
