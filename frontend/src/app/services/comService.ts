import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

@Injectable()
export class ComService {

  private comURL = 'http://localhost:8000/api/v1/compressor/?format=json';

  constructor(private http: Http) { }

  getEffect() {
    return this.http.get(this.comURL)
              .toPromise()
              .then(response => response.json())
              .catch(this.handleError);
  }

  private handleError(error: any) {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }
}