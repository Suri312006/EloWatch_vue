<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

<script setup>
import {onMounted} from 'vue'
import axios from 'axios'
import {useRoute} from 'vue-router'
import {reactive} from 'vue'

onMounted(() =>{
  test()
})

function test(){
  console.log('getting profile')

  axios
      .get(`/query/test/`)
      .then(response=>{
        console.log('response:', response.data)
      })
      .catch(error =>{
        console.log('error', error)
      })
}
</script>