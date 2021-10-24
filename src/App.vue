<template>
  <v-app>
    <v-app-bar app color="black" dark dense>
      <v-toolbar-title class="font-weight-bold">{{state}}</v-toolbar-title>
      <ul class="d-flex align-center" v-for="item in menuItems[state]" :key="item.name">
        <li>
          <v-btn text class="title" active-class="hoge" v-bind:to="item.linkto">{{item.name}}</v-btn>
        </li>
      </ul>

      <v-spacer></v-spacer>

      <v-toolbar-title>遠藤ヒズミ ポータルサイト</v-toolbar-title>

      <v-btn href="https://github.com/EndoHizumi" target="_blank" text>
        <v-icon large>mdi-github</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
      <div class="launcher">
        <span class="caption" v-bind:style="styleObject[hoveredIcon]">{{hoveredIcon}}</span>
        <div class="dock">
          <v-btn
            v-for="dockItem in dockItems"
            v-bind:key="dockItem.name"
            v-bind:id="dockItem.name"
            v-on:mouseover="hoveredIcon=dockItem.name"
            v-on:mouseleave="hoveredIcon=''"
            v-on:click="state=dockItem.name"
            text
            :to="linktoList[dockItem.name]"
          >
            <v-icon x-large>{{dockItem.icon}}</v-icon>
          </v-btn>
        </div>
      </div>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data: function () {
    return {
      draw: false,
      state: "Home",
      hoveredIcon: "",
      dockItems: [
        { name: "Profile", icon: "mdi-account" },
        { name: "Product", icon: "mdi-application" },
        { name: "Slide", icon: "mdi-presentation" },
        { name: "Writing", icon: "mdi-fountain-pen-tip" },
        { name: "Twitter", icon: "mdi-twitter" },
        { name: "Home", icon: "mdi-home" },
      ],
      menuItems: {
        Profile: [
          { name: "自己紹介", linkto: { name: "about" } },
          { name: "実績", linkto: { name: "about" } },
        ],
        Product: [
          { name: "webアプリ", linkto: { name: "webapps" } },
          { name: "フレームアームズ", linkto: { name: "framearms" } },
        ],
        Writing: [
          { name: "Qiita", linkto: { name: "about" } },
          { name: "Blog", linkto: { name: "about" } },
          { name: "技術同人誌", linkto: { name: "about" } },
        ],
      },
      styleObject: {
        Profile: { left: "28px" },
        Product: { left: "98px" },
        Slide: { left: "177px" },
        Writing: { left: "248px" },
        Twitter: { left: "318px" },
        Home: { left: "388px" },
      },
      linktoList: {
        Profile: { name: "about" },
        Product: { name: "webapp" },
        Slide: { name: "slide" },
        Writing: { name: "writing" },
        Twitter: { name: "twitter" },
        Home: { name: "home" },
      },
    };
  },
};
</script>

<style>
#app {
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