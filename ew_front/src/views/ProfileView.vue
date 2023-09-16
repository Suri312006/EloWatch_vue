

<template>
  <link href="https://fonts.googleapis.com/css2?family=Nova+Mono&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Nova+Mono&family=PT+Mono&display=swap" rel="stylesheet">

  <div class="bg-black grid grid-cols-12">
    <img
        src="https://opgg-static.akamaized.net/meta/images/profile_icons/profileIcon4656.jpg?image=q_auto,f_webp,w_auto&v=1694664078578"
        alt="penis"

        class="rounded col-span 2"
    >
    <div class="flex flex-col col-span-4">
      <h1 class="col-span-2 mt-4 ml-5 font-nova-pt-mono text-white text-5xl">SirYum</h1>
      <h1 class="ml-8 col-span-2 mt-3 ml-5 font-nova-mono text-white text-xl">Level 200</h1>
      <h1 class="ml-8 col-span-2 mt-3 ml-5 font-nova-mono text-white text-xl">Ladder Rank<span class="text-blue-400 text-glow"> 1 (top 100%)</span></h1>
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

<script setup>
import {onMounted} from 'vue'
import axios from 'axios'
import {useRoute} from 'vue-router'
import {reactive} from 'vue'

onMounted(() =>{
  getProfile()
})

//router var
const route = useRoute()

//plug in data
const summoner = reactive({
  summonerName : null,
  level : null,
  ladderRank : null,
  ladderRankPercent : null,
})


function getProfile(){
  console.log('getting profile')

  axios
      .get(`/query/profile/${route.params.name}/`)
      .then(response=>{
        console.log('response:', response.data)
      })
      .catch(error =>{
        console.log('error', error)
      })
}

</script>
