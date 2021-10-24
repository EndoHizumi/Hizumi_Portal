<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card class="mx-auto" outlined width="500px">
          <v-card-title class="font-weight-bold">自己紹介</v-card-title>
          <v-card-text class="text-left text-h6">
            <v-row>
              <v-col cols="9">
                <p>
                  ハンドルネーム：{{about.name}}
                  <br />
                  職業：{{about.job}}
                  <br />
                  生息地：{{about.location}}
                  <br />
                  好きな言語：{{about.favorite}}
                  <br />
                  好きなもの：{{about.hobby}}
                  <br />
                  座右の銘：{{about.motto}}
                </p>
              </v-col>
              <v-col cols="3">
                <v-img v-bind:src="loadPic()" height="100" contain></v-img>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
        <v-card class="mx-auto" outlined width="500px">
          <v-card-title class="font-weight-bold">人物紹介</v-card-title>
          <v-card-text class="text-h6">
            <p v-html="about.description"></p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import about from "../assets/about.json";
export default {
  data: function () {
    return {
      about: about,
    };
  },
  methods: {
    loadPic: function () {
      return require(`@/assets/${this.about.icon}`);
    },
  },
};
</script>

<style>
</style>