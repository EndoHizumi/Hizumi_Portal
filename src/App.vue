<template>
  <v-app>
    <v-app-bar app color="black" dark dense>
      <v-toolbar-title class="font-weight-bold">{{state}}</v-toolbar-title>
      <ul class="d-flex align-center" v-for="item in lists[state]" :key="item">
        <li>
          <v-btn text class="title">{{item}}</v-btn>
        </li>
      </ul>

      <v-spacer></v-spacer>

      <v-toolbar-title>遠藤ヒズミ ポータルサイト</v-toolbar-title>

      <v-btn href="https://github.com/EndoHizumi" target="_blank" text>
        <v-icon large>mdi-github</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <HelloWorld />
    </v-main>
    <div class="launcher">
      <span class="caption" v-bind:style="styleObject[hoveredIcon]">{{hoveredIcon}}</span>
      <div class="dock">
        <v-btn
          v-for="menuItem in menuItems"
          :key="menuItem.name"
          v-bind:id="menuItem.name"
          v-on:mouseover="hoveredIcon=menuItem.name"
          v-on:mouseleave="hoveredIcon=''"
          v-on:click="state=menuItem.name"
          text
        >
          <v-icon x-large>{{menuItem.icon}}</v-icon>
        </v-btn>
      </div>
    </div>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld";

export default {
  name: "App",

  components: {
    HelloWorld,
  },
  data: function () {
    return {
      draw: false,
      state: "Home",
      hoveredIcon: "",
      menuItems: [
        { name: "Profile", icon: "mdi-account" },
        { name: "Product", icon: "mdi-application" },
        { name: "Slide", icon: "mdi-presentation" },
        { name: "Writing", icon: "mdi-fountain-pen-tip" },
        { name: "Twitter", icon: "mdi-twitter" },
        { name: "Home", icon: "mdi-home" },
      ],
      lists: {
        Profile: ["自己紹介", "実績"],
        Product: ["ゲーム", "ツール", "Webサイト"],
        Writing: ["Qiita", "Blog", "技術同人誌"],
      },
      styleObject: {
        Profile: { left: "28px" },
        Product: { left: "98px" },
        Slide: { left: "177px" },
        Writing: { left: "248px" },
        Twitter: { left: "318px" },
        Home: { left: "388px" },
      },
    };
  },
};
</script>

<style>
#app{
  background-color: #1a1a1a;
  color: #f8f8f8;
}

ul {
  list-style: none;
  margin: 0px;
  padding: 0px;
}

.caption {
  width: 44px;
  display: inline-block;
  height: 14px;
  position: relative;
}

.launcher {
  position: absolute;
  height: 65px;
  width: 456px;
  bottom: 1.8%;
  left: 35%;
  right: 35%;
}

.dock {
  height: 85%;
  width: 100%;
  padding: 10px;
  background-color: rgba(248, 248, 248, 0.9);
}
</style>