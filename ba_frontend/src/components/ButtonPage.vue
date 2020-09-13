<template>
  <div class="ButtonPage">
    <h3>Welcome to the frontend page!</h3>
    <br />
    <br />
    <br />
    <input v-model="factorial_number_frontend" />
    <br />
    <br />
    <button type="button" @click="calcFactorialFrontend">factorize number (frontend)</button>
    <br />
    <br />-----------------------------------------
    <br />
    <br />
    <input v-model="factorial_number_backend" />
    <br />
    <br />
    <button type="button" @click="calcFactorialBackend">factorize number (backend)</button>
    <br />
    <br />-----------------------------------------
    <br />
    <br />
    <input v-model="simple_unsorted_string_size" />
    <input v-model="simple_unsorted_string_id" />
    <br />
    <br />
    <button type="button" @click="saveSimpleUnsortedString">Generate simple unsorted string</button>
    <button type="button" @click="sortSimpleUnsortedString">Sort string (frontend)</button>
    <br />
    <br />-----------------------------------------
    <br />
    <br />
    <input v-model="byte_size" />
    <input v-model="byte_id" />
    <br />
    <br />
    <button type="button" @click="saveBytes">Save zero bytes</button>
    <button type="button" @click="getBytes">Get zero bytes</button>
  </div>
</template>

<script>
import api from '@/api/api';

export default {
  name: 'ButtonPage',
  props: {},
  data() {
    return {
      factorial_number_frontend: 10,
      factorial_number_backend: 10,
      simple_unsorted_string_size: 10,
      simple_unsorted_string_id: 1,
      byte_size: 10,
      byte_id: 1,
    };
  },
  methods: {
    factorial(n) {
      return n !== 1 ? n * this.factorial(n - 1) : 1;
    },
    calcFactorialFrontend() {
      const start = Date.now();
      this.factorial(this.factorial_number_frontend);
      const end = Date.now();
      const duration = (end - start) / 1000;
      // eslint-disable-next-line
      alert(
        `duration: ${duration} seconds; number: ${this.factorial_number_frontend}`,
      );
    },
    async calcFactorialBackend() {
      const response = await api.getFactorial(this.factorial_number_backend);
      // eslint-disable-next-line
      alert(
        `duration: ${response.duration} seconds; number: ${this.factorial_number_backend}`,
      );
    },
    async saveSimpleUnsortedString() {
      const response = await api.saveSimpleUnsortedString(
        this.simple_unsorted_string_size,
      );
      this.simple_unsorted_string_id = response.id;
      // eslint-disable-next-line
      alert(
        `duration: ${response.duration} seconds; Size in MB: ${response.Actual_size_of_array_in_mb}`,
      );
    },
    async sortSimpleUnsortedString() {
      const response = await api.getString(this.simple_unsorted_string_id);
      const responseString = response.string;
      const start = Date.now();
      const stringArray = responseString.split('');
      stringArray.sort();
      const sortedString = stringArray.toString();
      const end = Date.now();
      const duration = (end - start) / 1000;
      // eslint-disable-next-line
      alert(
        `duration: ${duration} seconds; first element: ${
          sortedString[0]
        }, last element ${sortedString[sortedString.length - 1]}`,
      );
    },
    async saveBytes() {
      const response = await api.saveBytes(
        this.byte_size,
      );
      this.byte_id = response.id;
      // eslint-disable-next-line
      alert(
        `duration: ${response.duration} seconds; Size in MB: ${response.actual_size_of_bytes_in_mb}`,
      );
    },
    async getBytes() {
      const start = Date.now();
      const response = await api.getBytes(this.byte_id);
      const end = Date.now();
      const duration = (end - start) / 1000;
      // eslint-disable-next-line
      alert(
        `Duration of transfer(ca.):${
          duration - response.duration
        } seconds; Size in MB: ${response.size_of_bytes_in_mb}`,
      );
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
