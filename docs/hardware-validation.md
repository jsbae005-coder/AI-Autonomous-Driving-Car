# Hardware Discovery and Validation Checklist

Hardware details are currently unknown. Complete this checklist before
connecting firmware to a physical vehicle.

## Identify components

- [ ] Exact Arduino board model and revision
- [ ] Motor driver model and rated voltage/current
- [ ] Motor count, type, and left/right wiring
- [ ] HuskyLens firmware/version if available
- [ ] HuskyLens interface: UART or I2C
- [ ] Battery chemistry, voltage, and current capability
- [ ] Common-ground and power-regulator arrangement
- [ ] Emergency-stop method

## Verify communication

- [ ] Confirm the selected HuskyLens protocol from its official documentation
- [ ] Confirm baud rate or I2C address
- [ ] Confirm packet parsing with motors disconnected
- [ ] Handle invalid, incomplete, and stale sensor observations

## Safe bring-up sequence

1. Inspect wiring with the battery disconnected.
2. Power the controller and sensor without motor power.
3. Verify sensor communication and log received observations.
4. Test each motor output with wheels lifted and a current-limited supply.
5. Verify motor direction and stop behaviour.
6. Test emergency stop before closed-loop operation.
7. Begin at low speed in a clear, controlled test area.
8. Record repeatable trials before reporting performance.

Do not connect motors or batteries based on guessed pinouts or assumed board
models. Do not publish performance numbers until measured on the physical
vehicle.
