
<template>
  <v-card class="pa-6 mx-auto" elevation="6" max-width="400">
    <v-card-title class="text-h5 text-center">Number to English Converter</v-card-title>
    <v-card-text>
      <v-text-field v-model="number" label="Enter a number" outlined dense hide-details></v-text-field>
      <v-alert v-if="error" type="error" dense>{{ error }}</v-alert>
    </v-card-text>
    <v-card-actions class="justify-center">
      <v-btn @click="convertNumber('get')" color="primary">Convert (GET)</v-btn>
      <v-btn @click="convertNumber('post')" color="success">Convert (POST)</v-btn>
    </v-card-actions>
    <v-card-text v-if="loading" class="text-center text-grey">Loading...</v-card-text>
    <v-card-text v-if="result" class="text-center text-h6 font-weight-bold">{{ result }}</v-card-text>
  </v-card>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      number: '',
      result: '',
      error: '',
      loading: false,
    };
  },
  methods: {
    async convertNumber(method) {
      this.error = '';
      this.result = '';
      if (!this.number) {
        this.error = 'Please enter a valid number';
        return;
      }
      
      this.loading = method === 'post';
      try {
        const response = await (method === 'get' 
          ? axios.get(`http://localhost:8000/num_to_english?number=${this.number}`)
          : axios.post('http://localhost:8000/num_to_english', { number: this.number })
        );
        
        if (method === 'post') {
          setTimeout(() => {
            this.result = response.data.num_in_english;
            this.loading = false;
          }, 5000);
        } else {
          this.result = response.data.num_in_english;
        }
      } catch (err) {
        this.error = err.response?.data?.message || 'An error occurred';
        this.loading = false;
      }
    }
  }
};
</script>