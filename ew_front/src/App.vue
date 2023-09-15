<template>

    <link href="https://fonts.googleapis.com/css2?family=Nova+Mono&display=swap" rel="stylesheet">



  <div  class="bg-black py-4 text-white text-center font-nova-mono text-4xl">
    <RouterLink to="/">
        EloWatch
    </RouterLink>
  </div>

  <main class="px-8 py-6 bg-gray-100">
      <RouterView />
  </main>

  <Toast />
</template>

<style scoped>
/* Add any additional styling you want for your toolbar here */
.font-nova-mono {
  font-family: 'Nova Mono', monospace;
  /* You can adjust the font size, letter spacing, and other properties here */
  letter-spacing: 2px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}
</style>


<script>
  import axios from 'axios'
  import Toast from '@/components/Toast.vue'
  import { useUserStore } from '@/stores/user'

  export default {
      setup() {
          const userStore = useUserStore()

          return {
              userStore
          }
      },

      components: {
          Toast
      },

      beforeCreate() {
          this.userStore.initStore()

          const token = this.userStore.user.access

          if (token) {
              axios.defaults.headers.common["Authorization"] = "Bearer " + token;
          } else {
              axios.defaults.headers.common["Authorization"] = "";
          }
      }
  }
</script>