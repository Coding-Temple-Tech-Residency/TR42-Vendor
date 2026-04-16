import { ReactNode, useState } from "react";

type WorkOrderStatus =
    | "pending"
    | "assigned"
    | "in_progress"
    | "completed"
    | "cancelled"

type PriorityStatus = "low" | "medium" | "high" | "urgent";

type SelectOption = {
    value: string;
    label: string;
};

type EditWorkOrderFormData = {
    description: string;
    assigned_vendor: string;
    due_date: string;
    estimated_start_date: string;
    estimated_end_date: string;
    current_status: WorkOrderStatus;
    priority: PriorityStatus;
    comments: string;
    location: string;
    estimated_cost: string;
    estimated_duration: string;
    well_id: string;
};

type EditWorkOrderFormErrors = Partial<
    Record<keyof EditWorkOrderFormData, string>
>;

type EditWorkOrderFormProps = {
    description?: string;
    assigned_vendor?: string;
    due_date?: string;
    estimated_start_date?: string;
    estimated_end_date?: string;
    current_status?: WorkOrderStatus;
    priority?: PriorityStatus;
    comments?: string;
    location?: string;
    estimated_cost?: string;
    estimated_duration?: string;
    well_id?: string;
    vendorOptions?: SelectOption[];
    wellOptions?: SelectOption[];
    onSave?: (data: EditWorkOrderFormData) => void;
};

const statusOptions: SelectOption[] = [
    {value: "pending", label: "Pending"},
    {value: "assigned", label: "Assigned"},
    {value: "in_progress", label: "In Progress"},
    {value: "completed", label: "Completed"},
    {value: "cancelled", label: "Cancelled"},
];

const priorityOptions: SelectOption[] = [
    {value: "low", label: "Low"},
    {value: "medium", label: "Medium"},
    {value: "high", label: "High"},
    {value: "urgent", label: "Urgent"},
];

type SectionTitleProps = {
    title: string;
};

function SectionTitle({ title }: SectionTitleProps) {
    return (
        <h4 className="mb-3 text-sm font-semibold uppercase tracking-wide text-[#2F4F75]">{title}</h4>
    );
}

type FieldCardProps = {
    children: ReactNode;
    className?: string;
};

function FieldCard({ children, className = "" }: FieldCardProps) {
    return (
        <div className={`rounded-xl bg-[#C9D8E6] p-4 shadow-md ${className}`}>{children}</div>
    );
}

type FieldLabelProps = {
    label: string;
    required?: boolean;
};

function FieldLabel({ label, required = false }: FieldLabelProps) {
    return (
        <label className="text-xs font-medium uppercase tracking-wide text-[#2F4F75]">
            {label}
            {required && <span className="ml-1 text-red-500">*</span>}
        </label>
    );
}

type FieldErrorProps = {
    message?: string;
};

function FieldError({ message }: FieldErrorProps) {
    if(!message) return null;
}

type BaseFieldWrapperProps = {
    label: string;
    required?: boolean;
    error?: string;
    children: ReactNode;
    className?: string;
};

function BaseFieldWrapper({
    label,
    required = false,
    error,
    children,
    className = "",
}: BaseFieldWrapperProps) {
    return (
        <FieldCard className={className}>
            <FieldLabel label={label} required={required} />
            <div className="mt-2">{children}</div>
            <FieldError message={error} />
        </FieldCard>
    );
}

type TextInputFieldProps = {
    label: string;
    value: string;
    onChange: (value: string) => void
    required?: boolean;
    error?: string;
    type?: "text" | "number" | "date";
    placeholder?: string;
    className?: string;
}

function TextInputField({
    label,
    value,
    onChange,
    required = false,
    error,
    type = "text",
    placeholder,
    className = "",
}: TextInputFieldProps) {
    return (
        <BaseFieldWrapper
            label={label}
            required={required}
            error={error}
            className={className}
        >
            <input
                type={type}
                value={value}
                onChange={(e) => onChange(e.target.value)}
                required={required}
                placeholder={placeholder}
                className="w-full rounded-lg border border[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75]"
            />
        </BaseFieldWrapper>
    );
}

type TextareaFieldProps = {
    label: string;
    value: string;
    onChange: (value: string) => void;
    required?: boolean;
    error?: string;
    rows?: number;
    placeholder?: string;
    className?: string;
};

function TextareaField({
    label,
    value,
    onChange,
    required = false,
    error,
    rows = 4,
    placeholder,
    className = "",
}: TextareaFieldProps) {
    return (
        <BaseFieldWrapper
            label={label}
            required={required}
            error={error}
            className={className}
        >
            <textarea
                value={value}
                onChange={(e) => onChange(e.target.value)}
                required={required}
                rows={rows}
                placeholder={placeholder}
                className="w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75]"
            />
        </BaseFieldWrapper>
    );
}

type SelectFieldProps = {
    label: string;
    value: string;
    onChange: (value: string) => void;
    options: SelectOption[];
    required?:boolean;
    error?: string;
    placeholder?: string;
    className?: string;
};

function SelectField({
    label,
    value,
    onChange,
    options,
    required = false,
    error,
    placeholder,
    className = "",
}: SelectFieldProps) {
    return (
        <BaseFieldWrapper
            label={label}
            required={required}
            error={error}
            className={className}
        >
            <select
                value={value}
                onChange={(e) => onChange(e.target.value)}
                required={required}
                className="w-full rounded-lg border border-[#2F4F75] bg-white px-3 py-2 text-sm text-[#2F4F75]"
            >
                {placeholder && <option value="">{placeholder}</option>}
                {options.map((option) => (
                    <option key={option.value} value={option.value}>
                        {option.label}
                    </option>
                ))}
            </select>
        </BaseFieldWrapper>
    );
}

export default function WorkOrderForm({
    description = "",
    assigned_vendor = "",
    due_date = "",
    estimated_start_date= "",
    estimated_end_date = "",
    current_status = "pending",
    priority = "medium",
    comments = "",
    location = "",
    estimated_cost = "",
    estimated_duration = "",
    well_id = "",
    vendorOptions = [],
    wellOptions = [],
    onSave,
}: EditWorkOrderFormProps) {
    const [formData, setFormData] = useState<EditWorkOrderFormData>({
        description,
        assigned_vendor,
        due_date,
        estimated_start_date,
        estimated_end_date,
        current_status,
        priority,
        comments,
        location,
        estimated_cost,
        estimated_duration,
        well_id,
    });

    const [errors, setErrors] = useState<EditWorkOrderFormErrors>({})
    const [showConfirm, setShowConfirm] = useState(false);

    const handleChange = (
        field: keyof EditWorkOrderFormData,
        value: string
    ) => {
        setFormData((prev) => ({
            ...prev,
            [field]: value,
        }));

        setErrors((prev) => ({
            ...prev,
            [field]: undefined,
        }));
    };

    const validateForm = (): EditWorkOrderFormErrors => {
        const newErrors: EditWorkOrderFormErrors = {};

        if (!formData.description.trim()) {
            newErrors.description = "Description is required.";
        }

        if (!formData.assigned_vendor) {
            newErrors.assigned_vendor = "Assigned vendor is required.";
        }

        if (!formData.current_status) {
            newErrors.current_status = "Current status is required.";
        }

        if (!formData.location.trim()) {
            newErrors.location = "Location is required";
        }

        if (!formData.well_id) {
            newErrors.well_id = "Well ID is required.";
        }

        return newErrors;
    };

    const handleSubmit = () => {
        const newErrors = validateForm();

        if (Object.keys(newErrors).length > 0) {
            setErrors(newErrors);
            return;
        }

        setShowConfirm(true);
    };

    const confirmSave = () => {
        console.log("Saved Work Order Data:", formData);
        onSave?.(formData);
        setShowConfirm(false);
    };

    const cancelSave = () => {
        setShowConfirm(false);
    };

    return (
        <section className="mx-12 mt-12 rounded-2xl border border-[#2F4F75] bg-white p-6 shadow-lg">
            <div className="mb-6">
                <h3 className="text-lg text-[#2F4F75]">Edit Work Order</h3>
            </div>

            <div className="space-y-6">
                {/*Work Order Details*/}
                <div>
                    <SectionTitle title = "Work Order Details" />

                    <div className="grid gap-4 sm:grid-cols-2">
                        <TextareaField
                            label="Description"
                            value={formData.description}
                            onChange={(value) => handleChange("description", value)}
                            required
                            error={errors.description}
                            rows={4}
                            placeholder="Edit work order details"
                            className="sm:col-span-2"
                        />

                        <SelectField
                            label="Current Status"
                            value={formData.current_status}
                            onChange={(value) => handleChange("current_status", value)}
                            options={statusOptions}
                            required
                            error={errors.current_status}
                        />

                        <SelectField
                            label="Priority"
                            value={(value) => handleChange("priority", value)}
                            options={priorityOptions}
                            error={errors.priority}
                        />
                    </div>
                </div>

                <div>
                    <SectionTitle title="Assignment" />

                    <div className="grid gap-4 sm:grid-cols-2">
                        <SelectField
                            label="Assigned Vendor"
                            value={formData.assigned_vendor}
                            onChange={(value) => handleChange("assigned_vendor", value)}
                            options={vendorOptions}
                            placeholder="Select a vendor"
                            required
                            error={errors.assigned_vendor}
                        />

                        <div>
                            <SelectField
                                label="Well"
                                value={formData.well_id}
                                onChange={(value) => handleChange("well_id", value)}
                                options={wellOptions}
                                placeholder="Select a well"
                                required
                                error={errors.well_id}

                            />

                        </div>
                    </div>
                </div>

                <div>
                    <SectionTitle title="Schedule" />

                    <div className="grid gap-4 sm:grid-cols-2">
                        <TextInputField
                            label="Due Date"
                            type="date"
                            value={formData.due_date}
                            onChange={(value) => handleChange("due_date", value)}
                            error={errors.due_date}
                        />

                        <TextInputField
                            label="Estimated Start Date"
                            type="date"
                            value={formData.estimated_start_date}
                            onChange={(value) => handleChange("estimated_start_date", value)}
                            error={errors.estimated_start_date}

                        />

                        <TextInputField
                            label="Estimated End Date"
                            type="date"
                            value={formData.estimated_end_date}
                            onChange={(value) => handleChange("estimated_end_date", value)}
                            error={errors.estimated_end_date}
                        />

                        <TextInputField
                            label="Estimated Duration"
                            value={formData.estimated_duration}
                            onChange={(value) => handleChange("estimated_duration", value)}
                            placeholder="ex. 8 hours"
                            error={errors.estimated_duration}
                        />
                    </div>
                </div>

                <div>
                    <SectionTitle title="Location & Costs" />

                    <div className="grid gap-4 sm:grid-cols-2">
                        <TextInputField
                            label="Location"
                            value={formData.location}
                            onChange={(value) => handleChange("location", value)}
                            required
                            error={errors.location}
                        />

                        <TextInputField
                            label="Estimated Cost"
                            type="number"
                            value={formData.estimated_cost}
                            onChange={(value) => handleChange("estimated_cost", value)}
                            error={errors.estimated_cost}
                        />
                    </div>
                </div>

                <div>
                    <SectionTitle title="Additional Notes" />

                    <div className="grid gap-4 sm:grid-cols-2">
                        <TextareaField
                            label="Comments"
                            value={formData.comments}
                            onChange={(value) => handleChange("comments", value)}
                            rows={4}
                            placeholder="Add any notes or comments"
                            className="sm:col-span-2"
                        />
                    </div>
                </div>

                <div className="mt- flex justify-end">
                    <button
                        type="button"
                        onClick={handleSubmit}
                        className="rounded-xl bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#4A6C8A]"
                    >
                        Edit Work Order
                    </button>
                </div>

                {showConfirm && (
                    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
                    <div className="w-full max-w-md rounded-2xl bg-white p-6 shadow-xl">
                        <h3 className="text-lg font-semibold text-[#2F4F75]">
                        Confirm Work Order
                        </h3>

                        <p className="mt-2 text-sm text-[#4A6C8A]">
                        Are you sure you want to create this work order?
                        </p>

                        <div className="mt-6 flex justify-end gap-3">
                        <button
                            type="button"
                            onClick={cancelSave}
                            className="rounded-lg border border-[#2F4F75] px-4 py-2 text-sm text-[#2F4F75] hover:bg-[#4A6C8A] hover:text-white"
                        >
                            Cancel
                        </button>

                        <button
                            type="button"
                            onClick={confirmSave}
                            className="rounded-lg bg-[#2F4F75] px-4 py-2 text-sm font-medium text-white hover:bg-[#4A6C8A]"
                        >
                            Confirm
                        </button>
                        </div>
                    </div>
                    </div>
                )}
            </div>
        </section>
    );
}