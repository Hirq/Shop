import { Component, OnInit } from '@angular/core';
import { EffectService } from '../../services/effectService'
import { ComService } from '../../services/comService'
import { DisService } from '../../services/disService'
import { OctService } from '../../services/octService'

@Component({
  selector: 'app-elements',
  templateUrl: './elements.component.html',
  styleUrls: ['./elements.component.scss']
})
export class ElementsComponent implements OnInit {

  effects: any[];
  compressors: any[];
  distortions: any[];
  octavers:any[];
  error: any;

  constructor(private effectService: EffectService, private comService: ComService, private disService: DisService, private octService: OctService) {
    
   }

  getEffect() {
    this.effectService
      .getEffect()
      .then(effects => this.effects = effects)
      .catch(error => this.error = error);
    
    this.comService
      .getEffect()
      .then(compressors => this.compressors = compressors)
      .catch(error => this.error = error);

    this.disService
      .getEffect()
      .then(distortions => this.distortions = distortions)
      .catch(error => this.error = error);

    this.octService
      .getEffect()
      .then(octavers => this.octavers = octavers)
      .catch(error => this.error = error);
}


  ngOnInit() {
    this.getEffect();
  }

}
