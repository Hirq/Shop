import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

@Injectable()
export class OctService {

  private octURL = 'http://localhost:8000/api/v1/octave/?format=json';

  constructor(private http: Http) { }

  getEffect() {
    return this.http.get(this.octURL)
              .toPromise()
              .then(response => response.json())
              .catch(this.handleError);
  }

  private handleError(error: any) {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }
}