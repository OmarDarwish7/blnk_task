import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PersonnelHomeComponent } from './personnel-home.component';

describe('PersonnelHomeComponent', () => {
  let component: PersonnelHomeComponent;
  let fixture: ComponentFixture<PersonnelHomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PersonnelHomeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PersonnelHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
