import flax.linen as nn
from flax.serialization import msgpack_serialize, to_bytes
from pathlib import Path
from typing import Optional, Any

def dump_state(
    model: nn.Module,
    checkpoints_dir: str,
    step: int,
    optimizer_state: Optional[Any] = None,
    last_checkpoint: Optional[Path] = None,
):
    """
    Dumps the state of the model and optimizer to a checkpoint file.

    Args:
        model: The model to save.
        checkpoints_dir: The directory to save the checkpoint to.
        step: The current step number.
        optimizer_state: The optimizer state to save.
        last_checkpoint: The path to the last checkpoint, to be removed.
    """
    state_dict = {
        "step": step,
        "model_state": to_bytes(model.state_dict()),
    }
    if optimizer_state is not None:
        state_dict["optimizer_state"] = msgpack_serialize(optimizer_state)

    checkpoints_dir = Path(checkpoints_dir)
    checkpoints_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = checkpoints_dir / f"checkpoint_{step}.msgpack"

    with open(checkpoint_path, "wb") as f:
        f.write(msgpack_serialize(state_dict))

    if last_checkpoint and last_checkpoint.exists():
        last_checkpoint.unlink()
