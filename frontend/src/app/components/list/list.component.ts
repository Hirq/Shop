import { Component, OnInit } from '@angular/core';
import { EffectService } from '../../services/effectService'

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {

  effects: any[];
  error: any;

  constructor(private effectService: EffectService) { }

  getEffect() {
    this.effectService
      .getEffect()
      .then(effects => this.effects = effects)
      .catch(error => this.error = error);
  }

  ngOnInit() {
    this.getEffect();
  }

}
