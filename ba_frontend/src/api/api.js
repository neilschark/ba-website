import axios from 'axios';

export default {
  async getFactorial(number) {
    return axios.get(`api/factorial/${number}`).then((response) => response.data);
  },
  async saveSimpleUnsortedString(simpleUnsortedStringSize) {
    return axios.post('api/create/simple-string', { max_string_size: simpleUnsortedStringSize }).then((response) => response.data);
  },
  async getString(strId) {
    return axios.get(`api/get/string/${strId}`).then((response) => response.data);
  },
  async saveBytes(byteSize) {
    return axios.post('api/create/zero-bytes', { max_byte_size: byteSize }).then((response) => response.data);
  },
  async getBytes(byteId) {
    return axios.get(`api/get/zero-bytes/${byteId}`).then((response) => response.data);
  },

};
