import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class WebService {

   readonly ROOT_URL = "http://localhost:8000";



  constructor(private http: HttpClient) { }

  get(uri:string){
    return this.http.get(`${this.ROOT_URL}/${uri}`);
  }

  getWithBody(uri:string, payload:Object){
    return this.http.get(`${this.ROOT_URL}/${uri}`,payload);
  }

  post(uri:string , payload:Object){
    return this.http.post(`${this.ROOT_URL}/${uri}`,payload);
  }

  patch(uri:string, payload:Object){
    return this.http.patch(`${this.ROOT_URL}/${uri}`, payload);
  }

  delete(uri:string,payload:Object){
    return this.http.delete(`${this.ROOT_URL}/${uri}`,payload);
  }

}
