// netlifyにホスティングしているSiteの名前とサムネイル、リンクを取得する
// それを描画する
vue
<template>
  <v-container>
    <v-row>
      <v-col cols="3" v-for="num in 15" v-bind:key="num">
        <v-card :elevation="2" ma-2>
          <v-img
            :src="require('../assets/logo.png')"
            style="border-radius: 100px"
            class="my-0"
            contain
            height="200"
          />
          <v-card-title> App Name </v-card-title>
          <v-card-text> description </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {};
</script>

<style>
</style>