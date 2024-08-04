import "@testing-library/jest-dom";
import fetchMock from "jest-fetch-mock";

fetchMock.enableMocks();
process.env.API_URL = "http://localhost:8080/api/v1/order/";
