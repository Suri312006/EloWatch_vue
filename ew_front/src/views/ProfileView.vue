

<template>
  <link href="https://fonts.googleapis.com/css2?family=Nova+Mono&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Nova+Mono&family=PT+Mono&display=swap" rel="stylesheet">

  <div class="bg-black grid grid-cols-12">
    <img
        :src="summoner.icon_path"
        alt="penis"

        class="rounded col-span 2"
    >
    <div class="flex flex-col col-span-4">
      <h1 class="col-span-2 mt-2 ml-5 font-nova-pt-mono text-white text-5xl" >{{ summoner.name}}</h1>
      <h1 class="ml-8 col-span-2 mt-2 ml-5 font-nova-mono text-white text-xl"  >Level {{ summoner.level }}</h1>
      <h1 class="ml-8 col-span-2 mt-1 ml-5 font-nova-mono text-white text-l" >Top <span class="text-blue-400 text-glow"> {{ summoner.ladder_rank_percentage }}%</span></h1>
    </div>

    <div v-if="summoner" class="col-span-2">
      <Rank v-bind:rank_data="summoner.rank"/>
    </div>
  </div>
</template>

<style scoped>
/* Add any additional styling you want for your search bar here */
/* Add any additional styling you want for your toolbar here */
.font-nova-mono {
  font-family: 'Nova Mono', monospace;
  /* You can adjust the font size, letter spacing, and other properties here */
  letter-spacing: 0px;

}
.text-glow{
  text-shadow: 2px 2px 3px rgba(255, 255, 255, 0.5);
}
.font-nova-pt-mono{

font-family: 'PT Mono', monospace;

}
</style>

<script>
import axios from 'axios'
import Rank from '@/components/Rank.vue'
export default {
  name: 'ProfileView',
  data() {
    return {
      summoner: {
        name: null,
        level: null,
        rank: null,
        ladder_rank_percentage: null,
        icon_path: null
      }
    }
  },
  components: {
    Rank

  },

  mounted() {
    this.getProfile()
  },

  methods: {
    getProfile() {
      console.log('getting profile')

      axios
          .get(`/query/profile/${this.$route.params.name}/`)
          .then(response => {

            this.summoner = response.data.summoner
            console.log('summoner', this.summoner)
            console.log('rank', this.summoner.rank)
          })
          .catch(error => {
            console.log('error', error)
          })

    }
  }
}
</script>

<!--<script setup>-->
<!--import {onMounted} from 'vue'-->
<!--import axios from 'axios'-->
<!--import {useRoute} from 'vue-router'-->
<!--import {reactive} from 'vue'-->
<!--import { onBeforeMount } from 'vue'-->


<!--onBeforeMount(() =>{-->
<!--  getProfile()-->
<!--})-->

<!--//router var-->
<!--const route = useRoute()-->

<!--//plug in data-->
<!--let summoner = reactive({-->
<!--  name : null,-->
<!--  level : null,-->
<!--  rank : null,-->
<!--  ladder_rank_percentage : null,-->
<!--})-->


<!--function getProfile(){-->
<!--  console.log('getting profile')-->

<!--  axios-->
<!--      .get(`/query/profile/${route.params.name}/`)-->
<!--      .then(response=>{-->

<!--        summoner = response.data.summoner-->
<!--        console.log(summoner)-->
<!--      })-->
<!--      .catch(error =>{-->
<!--        console.log('error', error)-->
<!--      })-->
<!--}-->

<!--</script>-->