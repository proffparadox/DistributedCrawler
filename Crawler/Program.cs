using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace NetCore.Docker {
   public class Program {
        static HttpClient client = new HttpClient();
        static async Task<string> getToken() {
            string token = "";
            HttpResponseMessage response = await client.GetAsync("api/register");
            if (response.IsSuccessStatusCode) {
                token = await response.Content.ReadAsStringAsync();
            }
            return token;
        }

        static async Task<List<Uri>> GetUrisAsync(string token) {
            var uris = new List<Uri>();
            string json = "";
            HttpResponseMessage response = await client.GetAsync($"api/getJobs&token={token}");
            if (response.IsSuccessStatusCode) {
                 json = await response.Content.ReadAsStringAsync();
            }
        }

        static void Main(string[] args) {
            RunAsync().GetAwaiter().GetResult();
        }
        
        static async Task RunAsync() {
            client.BaseAddress = new Uri("www.laserbeam897.co.uk");
            client.DefaultRequestHeaders.Accept.Clear();
            client.DefaultRequestHeaders.Accept.Add(
                new MediaTypeWithQualityHeaderValue("appplication/json"));
            string token = await getToken();
            
        }
     
    }
}


