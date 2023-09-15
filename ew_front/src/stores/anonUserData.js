// store/anonUserData.js
import { defineStore } from 'pinia';

export const useAnonUserStore = defineStore({
  id: 'anonUser',
  state: () => ({
    data: null,
  }),

  actions: {
    setAnonymousUserData(data) {
      this.data = data;
    },
  },
});
