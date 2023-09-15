<!-- YourComponent.vue -->
<template>
  <div>
    <div v-if="anonymousUserData">
      <!-- Display data from the store -->
      <p>{{ anonymousUserData.field1 }}</p>
      <p>{{ anonymousUserData.field2 }}</p>
      <!-- ... -->
    </div>
    <div v-else>
      <!-- Handle the case when data is not available -->
      <p>No data available.</p>
    </div>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useAnonUserStore } from '@/store/anonUserData';

export default {
  setup() {
    const anonUserStore = useAnonUserStore();

    return{
      anonUserStore
    },

    onMounted(() => {
      // Fetch the anonymous user data when the component is mounted
      // Example:
      console.log('mounted')
      axios.get('/api/hi')
        .then((response) => {
          anonUserDataStore.setAnonymousUserData(response.data);
        })
        .catch((error) => {
          console.error('Error fetching anonymous user data:', error);
        });
    });

    return { anonymousUserData };
  },
};
</script>
