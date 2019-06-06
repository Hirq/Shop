import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

@Injectable()
export class DisService {

  private disURL = 'http://localhost:8000/api/v1/distortion/?format=json';

  constructor(private http: Http) { }

  getEffect() {
    return this.http.get(this.disURL)
              .toPromise()
              .then(response => response.json())
              .catch(this.handleError);
  }

  private handleError(error: any) {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }
}