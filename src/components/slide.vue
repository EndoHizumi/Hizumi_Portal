<template>
  <v-app>
    <v-row dense>
      <v-col pa-0 ma-n5 cols="3" v-for="item in slide_element" v-bind:key="item">
        <v-sheet elevation="2" dark v-html="item.html"></v-sheet>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      slide_element: null,
    };
  },
  methods: {},
  async mounted() {
    const slideUrlList =
      "https://asia-northeast1-get-your-decks.cloudfunctions.net/get_silde_infos/endohizumi";
    const res = await axios.get(slideUrlList);
    this.slide_element = res.data
  },
};
</script>

<style>
</style>