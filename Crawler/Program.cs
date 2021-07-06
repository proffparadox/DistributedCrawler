using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using System.Text.Json;

namespace NetCore.Docker {
    public class Program {
        static HttpClient _client = new HttpClient();

        private static async Task<Token> GetToken() {
            string stoken = "";
            HttpResponseMessage response = await _client.GetAsync("api/register");
            if (response.IsSuccessStatusCode) {
                stoken = await response.Content.ReadAsStringAsync();
            }

            Token token = JsonSerializer.Deserialize<Token>(stoken);
            return token;
        }

        public static async Task<List<Urls>> GetUrisAsync(Token token) {
            var uris = new List<Urls>();
            string json = "";
            HttpResponseMessage response = await _client.GetAsync($"api/getJobs&token={token.token}");
            if (response.IsSuccessStatusCode) {
                 json = await response.Content.ReadAsStringAsync();
            }
            uris = JsonSerializer.Deserialize<List<Urls>>(json);
            return uris;
        }

        public static void Main(string[] args) {
            RunAsync().GetAwaiter().GetResult();
        }

        private static async Task RunAsync() {
            //_client.BaseAddress = new Uri("https://www.laserbeam897.co.uk");
            //_client.DefaultRequestHeaders.Accept.Clear();
            //_client.DefaultRequestHeaders.Accept.Add(
            //    new MediaTypeWithQualityHeaderValue("appplication/json"));
            //string token = await GetToken();

            var testList = new List<string>();
            testList.Add("www.google.com");
            testList.Add("www.amazon.co.uk");
            var urls = new Urls()
            {
                urls = testList
            };
            string json = JsonSerializer.Serialize(urls);
            Console.WriteLine(json);
        }
     
    }
}


